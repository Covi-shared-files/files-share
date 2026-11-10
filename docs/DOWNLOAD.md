# 下载与 Git LFS 说明

[返回首页](../README.md) · [完整资源目录](./CATALOG.md)

## 只下载需要的文件

从完整资源目录进入对应文件页面，使用 GitHub 提供的下载按钮。仓库包含较多 PDF，只需要少量资料时，无需克隆整个仓库。

下载后应实际打开文件，确认内容和版本。若得到的是 HTML 网页或短文本，而非可阅读的 PDF，请检查下载方式和错误提示。

## 克隆仓库

先安装 Git 与 [Git LFS](https://git-lfs.com/)，再执行：

```sh
git lfs install
git clone https://github.com/Covi-shared-files/files-share.git
cd files-share
git lfs pull
```

这会下载仓库中的普通 Git 文件及可获取的 LFS 文件，可能需要较多时间和磁盘空间。

如果已经克隆过仓库，可以在仓库目录执行：

```sh
git lfs install
git lfs pull
```

## 为什么有的 PDF 只有几行文本

以下文件在 Git 中存储的是 LFS 指针，实际内容由 Git LFS 单独保存：

| 文件 | 指针声明的实际文件大小 |
| --- | --- |
| [工程数学线性代数第六版](../Math/工程数学线性代数第六版.pdf) | 143,387,115 字节 |
| [离散数学及其应用](<../Math/离散数学及其应用(原书第6版).Kenneth.H.Rosen.pdf>) | 82,114,993 字节 |

指针通常包含 `version https://git-lfs.github.com/spec/v1`、`oid sha256:...` 和 `size ...`。它不是 PDF 本体，也不能通过修改扩展名还原。

仓库的 [`.gitattributes`](../.gitattributes) 为以上两个路径声明 LFS 跟踪规则。规则只负责说明如何处理文件，**不能证明远端 LFS 对象已经上传成功或当前可下载**。

若 `git lfs pull` 报对象不存在、配额或权限错误，请保留错误信息，通过 [Issue](https://github.com/Covi-shared-files/files-share/issues) 告知维护者，需由维护者核对对象和访问状态。

GitHub 的 ZIP 归档是否包含 LFS 实际内容取决于仓库设置，不能默认认为下载 ZIP 就能得到全部 PDF。参考 [GitHub 的 Git LFS 说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)。

## 贡献者维护 LFS

本仓库现有 PDF 混用了普通 Git 和 LFS。新增大文件前请先与维护者商量，优先提供可信的原始链接。若确定需要用 LFS，按[官方配置说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage)设置跟踪，并将 `.gitattributes` 和文件一同提交。

不要仅为统一格式就批量迁移全部 PDF 或重写历史。提交前应在干净的检出中验证新增文件可以下载、打开，并核对来源与使用条款。
