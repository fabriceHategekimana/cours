let SessionLoad = 1
if &cp | set nocp | endif
<<<<<<< Updated upstream
let s:cpo_save=&cpo
set cpo&vim
inoremap <C-Y> 
inoremap <C-L> <Right>
inoremap <C-W> :w
inoremap <C-D><C-D> <><Left>
inoremap <C-D> <><Left>
nnoremap  :!. ~/sh/g.sh 
nnoremap   .
nmap <silent> \w\m <Plug>VimwikiMakeTomorrowDiaryNote
nmap <silent> \w\y <Plug>VimwikiMakeYesterdayDiaryNote
nmap <silent> \w\t <Plug>VimwikiTabMakeDiaryNote
nmap <silent> \w\w <Plug>VimwikiMakeDiaryNote
nmap <silent> \w\i <Plug>VimwikiDiaryGenerateLinks
nmap <silent> \wi <Plug>VimwikiDiaryIndex
nmap <silent> \ws <Plug>VimwikiUISelect
nmap <silent> \wt <Plug>VimwikiTabIndex
nmap <silent> \ww <Plug>VimwikiIndex
nnoremap controlv :let collage= Collage(collage)
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nnoremap go Go
nnoremap gi Gi
nnoremap tn :tabnew .
nnoremap vp :vsp .
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <C-G> :!. ~/sh/g.sh 
nnoremap <F12> :!clear
nnoremap <F10> :!gedit %
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F8> :call LinkImage()
nnoremap <F3> :! ~/sh/mymake.sh 
nnoremap <F1> :call Vimrc()
inoremap  <><Left>
inoremap  <><Left>
inoremap  <Right>
inoremap  :w
inoremap  
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
vnoremap ét :call Task()
nnoremap éé "
nnoremap éo oO
nnoremap èè :mks!
xnoremap éspa :call MakeSpace()
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
set autowriteall
set background=dark
set backspace=indent,eol,start
set fileencodings=ucs-bom,utf-8,default,latin1
set formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
set helplang=fr
set ignorecase
set incsearch
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/plugged/swift.vim/,~/.vim/plugged/nerdtree/,~/.vim/plugged/vimwiki/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set smartcase
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set window=42
=======
>>>>>>> Stashed changes
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/cours/intelligence_artificielle/tps/1
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
<<<<<<< Updated upstream
$argadd ex2.md
edit test.r
=======
$argadd ~/.bashrc
edit ~/.bashrc
>>>>>>> Stashed changes
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 87 + 92) / 185)
exe 'vert 2resize ' . ((&columns * 97 + 92) / 185)
argglobal
<<<<<<< Updated upstream
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> <F6> :!Rscript % 
nnoremap <buffer> <F5> :!Rscript --verbose %
nnoremap <buffer> <F4> :!R
nnoremap <buffer> <F2> :call Note("r")
inoremap <buffer> ** %*%
xnoremap <buffer> éd :normal! ^x
xnoremap <buffer> éc :normal! I#
nnoremap <buffer> éc I#
inoremap <buffer> dataframe data.frame()<Left>
inoremap <buffer> else else{}<Up>
inoremap <buffer> function <-function(){}<Up><Up>I
inoremap <buffer> if if(){}2<Up>t)a
inoremap <buffer> matrix matrix(a, byrow=TRUE, ncol=)<Left>
inoremap <buffer> print print()<Left>
inoremap <buffer> return return()<Left>
inoremap <buffer> while while(){}<Up><Up>t{i
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=:#',:###,:##,:#
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
set conceallevel=2
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'r'
setlocal filetype=r
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=GetRIndent()
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,.
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
set relativenumber
setlocal relativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=fr_ch,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'r'
setlocal syntax=r
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 2 - ((1 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
2
normal! 0
wincmd w
argglobal
if bufexists("ex2.r") | buffer ex2.r | else | edit ex2.r | endif
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> <F6> :!Rscript % 
nnoremap <buffer> <F5> :!Rscript --verbose %
nnoremap <buffer> <F4> :!R
nnoremap <buffer> <F2> :call Note("r")
inoremap <buffer> ** %*%
xnoremap <buffer> éd :normal! ^x
xnoremap <buffer> éc :normal! I#
nnoremap <buffer> éc I#
inoremap <buffer> dataframe data.frame()<Left>
inoremap <buffer> else else{}<Up>
inoremap <buffer> function <-function(){}<Up><Up>I
inoremap <buffer> if if(){}2<Up>t)a
inoremap <buffer> matrix matrix(a, byrow=TRUE, ncol=)<Left>
inoremap <buffer> print print()<Left>
inoremap <buffer> return return()<Left>
inoremap <buffer> while while(){}<Up><Up>t{i
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=:#',:###,:##,:#
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
set conceallevel=2
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'r'
setlocal filetype=r
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=GetRIndent()
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,.
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
set relativenumber
setlocal relativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=fr_ch,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'r'
setlocal syntax=r
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 261 - ((33 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
261
normal! 053|
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 87 + 92) / 185)
exe 'vert 2resize ' . ((&columns * 97 + 92) / 185)
tabnext 1
badd +0 test.r
badd +1 ex2.md
badd +98 ex2.r
badd +5 ex1.r
badd +19 ~/note/note_r
badd +412 ~/.vimrc
=======
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 176 - ((24 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
176
normal! 04|
tabnext 1
badd +0 ~/.bashrc
>>>>>>> Stashed changes
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
