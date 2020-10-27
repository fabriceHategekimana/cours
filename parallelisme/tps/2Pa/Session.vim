let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <C-S> <Right>
inoremap <C-Y> 
inoremap <C-W> :w
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
nnoremap vs :sp .
nnoremap vp :vsp .
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <C-G> :!. ~/sh/g.sh 
nnoremap <F12> :!clear
nnoremap <F10> :!gedit %
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F7> :!make 
nnoremap <F3> :! ~/sh/mymake.sh 
nnoremap <F1> :call Vimrc()
inoremap  <Right>
inoremap  :w
inoremap  
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
nnoremap éé "
nnoremap éo oO
nnoremap èè :call Session()
xnoremap éspa :call MakeSpace()
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
set backspace=indent,eol,start
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=fr
set ignorecase
set incsearch
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/plugged/swift.vim/,~/.vim/plugged/nerdtree/,~/.vim/plugged/vimwiki/,~/.vim/plugged/syntastic/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set smartcase
set splitbelow
set splitright
set statusline=%#warningmsg#%{SyntasticStatuslineFlag()}%*
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/cours/parallelisme/tps/2Pa
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd tp2.cpp
set stal=2
tabnew
tabrewind
edit tp2.cpp
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <C-D> /_s
inoremap <buffer> <C-L> /_s
nnoremap <buffer> <F6> :let g:parallele= 
nnoremap <buffer> <F5> :call RunCpp()
xnoremap <buffer> <F5> y:call RunCppPart()
nnoremap <buffer> <F2> :call Note("cpp")
inoremap <buffer>  /_s
inoremap <buffer>  /_s
xnoremap <buffer> éd :normal ^xx
nnoremap <buffer> éd ^xx
xnoremap <buffer> éc :normal I//
nnoremap <buffer> éc I//$
inoremap <buffer> barri MPI_Barrier(MPI_COMM_WORLD);double start = MPI_Wtime();//execution de l'algorithmeMPI_Barrier(MPI_COMM_WORLD);double end = MPI_Wtime();if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;
inoremap <buffer> else else{}<Up>
inoremap <buffer> function int (_){}<Up><Up>f(i
inoremap <buffer> for for(int i= 0; i < n; i++){}<Up>
inoremap <buffer> if if(){}2<Up>t)a
inoremap <buffer> list std::list<int> 
inoremap <buffer> print std::cout <<  << std::endl;2F i
inoremap <buffer> recv MPI_Status status;MPI_Recv(&, sizeof(int), MPI_INT, i, 0, MPI_COMM_WORLD, &status);F&a
inoremap <buffer> send MPI_Send(&, sizeof(int), MPI_INT, i, 0, MPI_COMM_WORLD);F&a
inoremap <buffer> vsend MPI_Send(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
inoremap <buffer> vrecv MPI_Status status;MPI_Recv(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD, &status);
inoremap <buffer> vfor for(auto i: v)
inoremap <buffer> vector std::vector<int> (_, _);2F a
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
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^\\s*#\\s*define
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'cpp'
setlocal filetype=cpp
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
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*#\\s*include
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
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
setlocal omnifunc=ccomplete#Complete
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
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'cpp'
setlocal syntax=cpp
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
let s:l = 14 - ((0 * winheight(0) + 25) / 51)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
14
normal! 09|
tabnext
edit Array2D.hpp
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <C-D> /_s
nnoremap <buffer> <F6> :let g:parallele= 
nnoremap <buffer> <F5> :call RunCpp()
xnoremap <buffer> <F5> y:call RunCppPart()
nnoremap <buffer> <F2> :call Note("cpp")
inoremap <buffer>  /_s
xnoremap <buffer> éd :normal ^xx
nnoremap <buffer> éd ^xx
xnoremap <buffer> éc :normal I//
nnoremap <buffer> éc I//$
inoremap <buffer> barri MPI_Barrier(MPI_COMM_WORLD);double start = MPI_Wtime();//execution de l'algorithmeMPI_Barrier(MPI_COMM_WORLD);double end = MPI_Wtime();if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;
inoremap <buffer> else else{}<Up>
inoremap <buffer> function int (_){}<Up><Up>f(i
inoremap <buffer> for for(int i= 0; i < n; i++){}<Up>
inoremap <buffer> if if(){}2<Up>t)a
inoremap <buffer> list std::list<int> 
inoremap <buffer> print std::cout <<  << std::endl;2F i
inoremap <buffer> recv MPI_Status status;MPI_Recv(&, sizeof(int), MPI_INT, i, 0, MPI_COMM_WORLD, &status);F&a
inoremap <buffer> send MPI_Send(&, sizeof(int), MPI_INT, i, 0, MPI_COMM_WORLD);F&a
inoremap <buffer> vsend MPI_Send(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
inoremap <buffer> vrecv MPI_Status status;MPI_Recv(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD, &status);
inoremap <buffer> vfor for(auto i: v)
inoremap <buffer> vector std::vector<int> (_, _);2F a
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
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^\\s*#\\s*define
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'cpp'
setlocal filetype=cpp
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
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*#\\s*include
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
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
setlocal omnifunc=ccomplete#Complete
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
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'cpp'
setlocal syntax=cpp
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
let s:l = 12 - ((11 * winheight(0) + 25) / 51)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
12
normal! 044|
tabnext 1
set stal=1
badd +0 tp2.cpp
badd +0 Array2D.hpp
badd +1 .
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
