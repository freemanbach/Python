" Vim configuration file

" No more "vi" compatibility
set nocompatible

" General vim stuff
filetype plugin on
filetype indent on
syntax on
set nowrap

" Default color
colorscheme desert

autocmd FileType php set omnifunc=phpcomplete#CompletePHP

set backspace=indent,eol,start

" I don't want those .swp files cluttering up my normal directories
" Gets very messy with version control
" So store them in a seperate directory
set directory=~/.vim/swap-files,~/tmp,.

" VCL stuff, for editing Varnish files
au BufRead,BufNewFile *.vcl :set ft=vcl
au! Syntax vcl source ~/.vim/syntax/vcl.vim

" Parse the php-fpm.conf file as a dosini
autocmd BufRead,BufNewFile /etc/php-fpm.conf set syntax=dosini

" Show nice info in ruler
set ruler
set laststatus=2

" Set standard setting for PEAR coding standards
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set number

" Auto indenting is just so nice
set autoindent
set smartindent

" When searching in vim, make sure the search hit is never at the bottom
set scrolloff=5

" Source/reload .vimrc after saving .vimrc
autocmd bufwritepost .vimrc source $MYVIMRC

" Increase the history buffer for undo'ing mistakes
set history=1000
set undolevels=1000

" Enable at least 256 colors instead of the default 8 (I think?)
set t_Co=256
