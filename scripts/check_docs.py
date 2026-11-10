#!/usr/bin/env python3
"""Check checked-out Markdown links and PDF catalog coverage using the Git index."""

from __future__ import annotations

import posixpath
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CATALOG = "docs/CATALOG.md"
LINK = re.compile(r"\[[^\]\n]*\]\((?:<([^>\n]+)>|([^\s)]+))\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def index_entries() -> dict[str, str]:
    result = subprocess.run(
        ["git", "ls-files", "--stage", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    entries = {}
    for record in result.stdout.split(b"\0"):
        if not record:
            continue
        metadata, path = record.split(b"\t", 1)
        _, sha, stage = metadata.split()
        if stage != b"0":
            raise ValueError("Unmerged index entry: " + path.decode("utf-8"))
        entries[path.decode("utf-8")] = sha.decode("ascii")
    return entries


def destinations(markdown: str):
    fence = None
    for line in markdown.splitlines():
        marker = FENCE.match(line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            # These documents use inline links; code spans are not links.
            line = re.sub(r"`[^`]*`", "", line)
            for match in LINK.finditer(line):
                yield match.group(1) or match.group(2)


def local_target(document: str, destination: str) -> str | None:
    url = urlsplit(destination)
    if url.scheme or url.netloc or not url.path:
        return None
    path = unquote(url.path)
    # A leading slash on GitHub is site-relative, not repository-relative.
    if path.startswith("/"):
        return None
    return posixpath.normpath(posixpath.join(posixpath.dirname(document), path))


def main() -> int:
    try:
        entries = index_entries()
    except (subprocess.CalledProcessError, ValueError) as error:
        print(f"Cannot read Git index: {error}", file=sys.stderr)
        return 1

    paths = set(entries)
    directories = set()
    for path in paths:
        parent = posixpath.dirname(path)
        while parent:
            directories.add(parent)
            parent = posixpath.dirname(parent)

    errors = []
    checked = 0
    link_count = 0
    catalog_targets = set()
    for document in sorted(paths):
        source = ROOT / document
        if not document.lower().endswith(".md") or not source.is_file():
            continue
        checked += 1
        for destination in destinations(source.read_text(encoding="utf-8")):
            target = local_target(document, destination)
            if target is None:
                continue
            link_count += 1
            if target not in paths and target not in directories and target != ".":
                errors.append(f"{document}: missing target {destination}")
            if document == CATALOG:
                catalog_targets.add(target)

    if not (ROOT / CATALOG).is_file() or CATALOG not in paths:
        errors.append(f"Missing checked-out, staged catalog: {CATALOG}")
    else:
        for path in sorted(paths):
            if path.lower().endswith(".pdf") and path not in catalog_targets:
                errors.append(f"PDF missing from catalog: {path}")

    by_sha = defaultdict(list)
    for path, sha in entries.items():
        if path.lower().endswith(".pdf"):
            by_sha[sha].append(path)
    for duplicates in sorted(sorted(group) for group in by_sha.values() if len(group) > 1):
        print("INFO identical Git PDF blobs: " + " | ".join(duplicates))

    print(f"Checked {checked} Markdown files, {link_count} relative links, "
          f"{sum(path.lower().endswith('.pdf') for path in paths)} tracked PDFs.")
    if errors:
        for error in errors:
            print("ERROR " + error, file=sys.stderr)
        return 1
    print("OK: relative links and PDF catalog coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
