" 语法显示
filetype plugin indent on  " 初始化文件类型检测
syntax enable              " 启用语法高亮

" 适配优化
set nocompatible     " 禁用 Vi 兼容模式
set encoding=utf-8   " 设置编码

" 使用优化
set showmatch        " 匹配符号（括号等）
set number           " 显示行号
set ruler            " 右下角显示光标位置
set incsearch        " 找要匹配的单词
set autowrite        " 在每次修改后自动保存并退出
set cursorline       " 当前行高亮
set linebreak        " 不可拆词，除非遇到空格或连词符等
set laststatus=2     " 是否显示状态栏。0 表示不显示，1 表示只在多窗口时显示，2 表示显示
set ttimeoutlen=70   " ..某种..刷新时间？防止ecs会使终端失去焦点
set noundofile       " 保存撤销历史
filetype indent on   " 文件类型检测并载入缩进规则
set t_Co=256         " 256色模式
set showcmd          " 命令提示
"set spell spelllang=en_us,jck   " 拼写检测

" 防丢失策略
set nobackup         " 不在保存时自动创建备份
set swapfile         " 使用交换文件（防崩溃）

" 缩进设置
set tabstop=4        " 设置TAB=4（默认值是8）
set softtabstop=4    " 设置编辑模式时按退格键时退回缩进的长度
set autoindent     " 禁用自动缩进格式对齐
set expandtab        " 当设置成expandtab时，缩进用空格来表示
set shiftwidth=4     " 自动缩进空白字符个数(<<,>>,==)

" 搜索
set hlsearch         " 高亮显示搜索
set noincsearch      " 搜索模式输入自动跳转

" 字体与大小
set guifont=Courier_New:h30 " 注：本设置仅对GUI生效，终端字体仅能默认跟随系统终端设置

" 配色方案
colorscheme desert

" 设置帮助文本为中文（插件实现）
set helplang=cn

" 可选的选项
"
" set vb t_vb=   "取消命令错误的响声
" set cursorline " 设置游标
" set noswapfile " 不创建交换文件



" 插件选项
" ==================================
"set rtp+=~/.vim/bundle/Vundle.vim
" 启用插件管理器
call plug#begin('~/.vim/plugged')
" ----------------------------------
" 文件树插件
Plug 'preservim/nerdtree'

" 禁用netrw以避免冲突
let g:loaded_netrw = 1
let g:loaded_netrwPlugin = 1

" 核心配置：始终打开NERDTree但避免重复
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * 
    \ if argc() == 0 || (argc() == 1 && !isdirectory(argv()[0])) | 
    \   NERDTree | 
    \   wincmd p | 
    \ endif

" 处理目录参数的特殊情况
autocmd VimEnter * 
    \ if argc() == 1 && isdirectory(argv()[0]) | 
    \   execute 'NERDTree' fnameescape(argv()[0]) | 
    \   wincmd p | 
    \ endif

" 处理多个文件参数的情况
autocmd VimEnter * 
    \ if argc() > 1 | 
    \   NERDTree | 
    \   wincmd p | 
    \ endif

" 自动退出优化
autocmd BufEnter * 
    \ if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | 
    \   q | 
    \ endif

" 优化设置
let g:NERDTreeWinSize = 30
let g:NERDTreeShowHidden = 1
let g:NERDTreeChDirMode = 2  " 总是跟随当前文件目录

" ----------------------------------
"自动括号补全
Plug 'jiangmiao/auto-pairs'
" ----------------------------------
" 自动补全插件
" Plug 'ycm-core/YouCompleteMe'  "不会装....
" ----------------------------------
" 状态栏美化
Plug 'vim-airline/vim-airline'
" ----------------------------------
" 中文文档插件
Plug 'vimcn/vimcdoc'
" ----------------------------------
" Vundle插件管理
" Plugin 'gmarik/Vundle.vim'
" ==================================
call plug#end()
" NERDTree 配置（按 F3 开关文件树）
map <F3> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1  " 显示隐藏文件
" YouCompleteMe 基础设置
let g:ycm_auto_trigger = 1
let g:ycm_min_num_of_chars_for_completion = 2
let g:ycm_seed_identifiers_with_syntax = 1
