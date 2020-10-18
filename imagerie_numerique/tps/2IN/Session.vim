let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <C-Y> 
inoremap <C-L> <Right>
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
nnoremap <F8> :call LinkImage()
nnoremap <F3> :! ~/sh/mymake.sh 
nnoremap <F1> :call Vimrc()
inoremap  <Right>
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
set runtimepath=~/.vim,~/.vim/plugged/swift.vim/,~/.vim/plugged/nerdtree/,~/.vim/plugged/vimwiki/,~/.vim/plugged/syntastic/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set smartcase
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set statusline=%#warningmsg#%{SyntasticStatuslineFlag()}%*
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set wildignore=*.pyc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/cours/imagerie_numerique/tps/2IN
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd tp2.py
set stal=2
tabnew
tabrewind
edit tp2.py
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
inoremap <buffer> <C-S> <Right>
nnoremap <buffer> <F6> :call RunPythonLess()
xnoremap <buffer> <F5> y:call RunPythonPart()
nnoremap <buffer> <F5> :call RunPython()
nnoremap <buffer> <F4> :!python3
nnoremap <buffer> <F2> :call Note("py")
inoremap <buffer>  /_s
inoremap <buffer>  <Right>
nnoremap <buffer> éd ^x 
xnoremap <buffer> éd :normal ^x
xnoremap <buffer> éc :normal I#
nnoremap <buffer> éc ^i#
inoremap <buffer> class class ():def __init__(self):#code<Up><Up><Up><Left><Left><Left>
inoremap <buffer> def  def ():F(i
inoremap <buffer> for for i in range(0, n):
inoremap <buffer> npde np.linalg.det()<Left>
inoremap <buffer> npdo np.dot(,_)<Left><Left><Left>
inoremap <buffer> npa np.array([])<Left><Left>
inoremap <buffer> printg print("")<Left><Left>
inoremap <buffer> print print()<Left>
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
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
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
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
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},0),0],:,!^F,o,O,e,<:>,=elif,=except
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
setlocal omnifunc=python3complete#Complete
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
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
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
let s:l = 10 - ((9 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
10
normal! 0
tabnext
edit tp2IN_Hategekimana_Fabrice.md
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <expr> <S-Tab> vimwiki#tbl#kbd_shift_tab()
inoremap <buffer> <silent> <S-CR> :VimwikiReturn 2 2
imap <buffer> <silent> <C-L><C-M> <Plug>VimwikiListToggle
imap <buffer> <silent> <C-L><C-K> <Plug>VimwikiListPrevSymbol
imap <buffer> <silent> <C-L><C-J> <Plug>VimwikiListNextSymbol
imap <buffer> <silent> <C-T> <Plug>VimwikiIncreaseLvlSingleItem
imap <buffer> <silent> <C-D> <Plug>VimwikiDecreaseLvlSingleItem
nmap <buffer> <silent> 	 <Plug>VimwikiNextLink
vmap <buffer> <silent>  <Plug>VimwikiNormalizeLinkVisualCR
nmap <buffer> <silent>  <Plug>VimwikiFollowLink
nnoremap <buffer>  :!. ~/sh/cs.sh
vmap <buffer> <silent> + <Plug>VimwikiNormalizeLinkVisual
nmap <buffer> <silent> + <Plug>VimwikiNormalizeLink
nmap <buffer> <silent> - <Plug>VimwikiRemoveHeaderLevel
nmap <buffer> <silent> <D-CR> <Plug>VimwikiTabnewLink
nmap <buffer> <silent> = <Plug>VimwikiAddHeaderLevel
inoremap <buffer> ééfff \flechel{nom1}{nom2}{label}{angleIn}{angleOut}
inoremap <buffer> ééff \fleche{nom1}{nom2}{label}
inoremap <buffer> éér \rectangle{nom}{x}{y}
inoremap <buffer> ééim ![](images/num.png)^<Right>a
inoremap <buffer> ééd \begin{tikzpicture}\end{tikzpicture}
inoremap <buffer> ééta :call MarkdownLigne()
inoremap <buffer> éém ``<Left>
inoremap <buffer> ééco ``````<Left><Left><Left><Up>
inoremap <buffer> éésss I#### 
inoremap <buffer> ééss I### 
inoremap <buffer> éés I## 
inoremap <buffer> ééti # 
inoremap <buffer> ééit __<Left>
inoremap <buffer> ééb ****<Left><Left>
nnoremap <buffer> <silent> O :call vimwiki#lst#kbd_O()
nmap <buffer> <silent> [= <Plug>VimwikiGoToPrevSiblingHeader
nmap <buffer> <silent> [[ <Plug>VimwikiGoToPrevHeader
nmap <buffer> <silent> [u <Plug>VimwikiGoToParentHeader
nmap <buffer> <silent> \wr <Plug>VimwikiRenameLink
nmap <buffer> <silent> \wd <Plug>VimwikiDeleteLink
nmap <buffer> \whh <Plug>Vimwiki2HTMLBrowse
nmap <buffer> \wh <Plug>Vimwiki2HTML
nmap <buffer> <silent> ]= <Plug>VimwikiGoToNextSiblingHeader
nmap <buffer> <silent> ]] <Plug>VimwikiGoToNextHeader
nmap <buffer> <silent> ]u <Plug>VimwikiGoToParentHeader
vnoremap <buffer> <silent> al :call vimwiki#lst#TO_list_item(0, 1)
onoremap <buffer> <silent> al :call vimwiki#lst#TO_list_item(0, 0)
vnoremap <buffer> <silent> ac :call vimwiki#base#TO_table_col(0, 1)
onoremap <buffer> <silent> ac :call vimwiki#base#TO_table_col(0, 0)
vnoremap <buffer> <silent> a\ :call vimwiki#base#TO_table_cell(0, 1)
onoremap <buffer> <silent> a\ :call vimwiki#base#TO_table_cell(0, 0)
vnoremap <buffer> <silent> aH :call vimwiki#base#TO_header(0, 1, v:count1)
onoremap <buffer> <silent> aH :call vimwiki#base#TO_header(0, 1, v:count1)
vnoremap <buffer> <silent> ah :call vimwiki#base#TO_header(0, 0, v:count1)
onoremap <buffer> <silent> ah :call vimwiki#base#TO_header(0, 0, v:count1)
nnoremap <buffer> gww :VimwikiTableAlignW
nnoremap <buffer> gqq :VimwikiTableAlignQ
noremap <buffer> <silent> gL1 :VimwikiChangeSymbolInListTo 1.
noremap <buffer> <silent> gl1 :VimwikiChangeSymbolTo 1.
noremap <buffer> <silent> gL+ :VimwikiChangeSymbolInListTo +
noremap <buffer> <silent> gl+ :VimwikiChangeSymbolTo +
noremap <buffer> <silent> gL* :VimwikiChangeSymbolInListTo *
noremap <buffer> <silent> gl* :VimwikiChangeSymbolTo *
noremap <buffer> <silent> gL- :VimwikiChangeSymbolInListTo -
noremap <buffer> <silent> gl- :VimwikiChangeSymbolTo -
map <buffer> <silent> gL  <Plug>VimwikiRemoveCBInList
map <buffer> <silent> gl  <Plug>VimwikiRemoveSingleCB
map <buffer> <silent> gLL <Plug>VimwikiIncreaseLvlWholeItem
map <buffer> <silent> gLl <Plug>VimwikiIncreaseLvlWholeItem
map <buffer> <silent> gLH <Plug>VimwikiDecreaseLvlWholeItem
map <buffer> <silent> gLh <Plug>VimwikiDecreaseLvlWholeItem
map <buffer> <silent> gll <Plug>VimwikiIncreaseLvlSingleItem
map <buffer> <silent> glh <Plug>VimwikiDecreaseLvlSingleItem
nmap <buffer> <silent> gLR <Plug>VimwikiRenumberAllLists
nmap <buffer> <silent> gLr <Plug>VimwikiRenumberAllLists
nmap <buffer> <silent> glr <Plug>VimwikiRenumberList
vmap <buffer> <silent> glp <Plug>VimwikiDecrementListItem
nmap <buffer> <silent> glp <Plug>VimwikiDecrementListItem
vmap <buffer> <silent> gln <Plug>VimwikiIncrementListItem
nmap <buffer> <silent> gln <Plug>VimwikiIncrementListItem
vmap <buffer> <silent> glx <Plug>VimwikiToggleRejectedListItem
nmap <buffer> <silent> glx <Plug>VimwikiToggleRejectedListItem
vnoremap <buffer> <silent> il :call vimwiki#lst#TO_list_item(1, 1)
onoremap <buffer> <silent> il :call vimwiki#lst#TO_list_item(1, 0)
vnoremap <buffer> <silent> ic :call vimwiki#base#TO_table_col(1, 1)
onoremap <buffer> <silent> ic :call vimwiki#base#TO_table_col(1, 0)
vnoremap <buffer> <silent> i\ :call vimwiki#base#TO_table_cell(1, 1)
onoremap <buffer> <silent> i\ :call vimwiki#base#TO_table_cell(1, 0)
vnoremap <buffer> <silent> iH :call vimwiki#base#TO_header(1, 1, v:count1)
onoremap <buffer> <silent> iH :call vimwiki#base#TO_header(1, 1, v:count1)
vnoremap <buffer> <silent> ih :call vimwiki#base#TO_header(1, 0, v:count1)
onoremap <buffer> <silent> ih :call vimwiki#base#TO_header(1, 0, v:count1)
nnoremap <buffer> <silent> o :call vimwiki#lst#kbd_o()
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevSiblingHeader :call vimwiki#base#goto_sibling(-1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextSiblingHeader :call vimwiki#base#goto_sibling(+1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevHeader :call vimwiki#base#goto_prev_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextHeader :call vimwiki#base#goto_next_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToParentHeader :call vimwiki#base#goto_parent_header()
nnoremap <buffer> <silent> <Plug>VimwikiRemoveHeaderLevel :call vimwiki#base#RemoveHeaderLevel()
nnoremap <buffer> <silent> <Plug>VimwikiAddHeaderLevel :call vimwiki#base#AddHeaderLevel()
nmap <buffer> <silent> <M-Right> <Plug>VimwikiTableMoveColumnRight
nmap <buffer> <silent> <M-Left> <Plug>VimwikiTableMoveColumnLeft
vmap <buffer> <silent> <C-@> <Plug>VimwikiToggleListItem
vmap <buffer> <silent> <Nul> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-@> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <Nul> <Plug>VimwikiToggleListItem
vmap <buffer> <silent> <C-Space> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-Space> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-Up> <Plug>VimwikiDiaryPrevDay
nmap <buffer> <silent> <C-Down> <Plug>VimwikiDiaryNextDay
nmap <buffer> <silent> <S-Tab> <Plug>VimwikiPrevLink
nmap <buffer> <silent> <BS> <Plug>VimwikiGoBackLink
nmap <buffer> <silent> <C-S-CR> <Plug>VimwikiTabnewLink
nmap <buffer> <silent> <C-CR> <Plug>VimwikiVSplitLink
nmap <buffer> <silent> <S-CR> <Plug>VimwikiSplitLink
nnoremap <buffer> <F6> :call Imagerie()
nnoremap <buffer> <F5> :!bash ~/sh/compmd.sh % 
nnoremap <buffer> <F4> :let toc= Toc(toc)
nnoremap <buffer> <F2> :let note= Note("markdown")
nnoremap <buffer> <C-P> :!. ~/sh/cs.sh
imap <buffer> <silent>  <Plug>VimwikiDecreaseLvlSingleItem
inoremap <buffer> <expr> 	 vimwiki#tbl#kbd_tab()
imap <buffer> <silent>  <Plug>VimwikiListToggle
imap <buffer> <silent>  <Plug>VimwikiListPrevSymbol
imap <buffer> <silent> <NL> <Plug>VimwikiListNextSymbol
inoremap <buffer> <silent>  :VimwikiReturn 1 5
imap <buffer> <silent>  <Plug>VimwikiIncreaseLvlSingleItem
nnoremap <buffer> échant :call Chant()
xnoremap <buffer> ém di``<Left>p
nnoremap <buffer> ém bi`ea`
nnoremap <buffer> éim i![](images/num.png)^<Right>a
nnoremap <buffer> éta :call MarkdownLigne()
nnoremap <buffer> éco i``````<Left><Left><Left><Up>
xnoremap <buffer> éb di****2<Left>p
nnoremap <buffer> éb I**A**
nnoremap <buffer> ésss I#### 
nnoremap <buffer> éss I### 
nnoremap <buffer> és I## 
nnoremap <buffer> ét :call MarkdownTitre()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
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
setlocal comments=
setlocal commentstring=%%%s
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
if &filetype != 'vimwiki'
setlocal filetype=vimwiki
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
setlocal formatoptions=tqn
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
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
setlocal omnifunc=Complete_wikifiles
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
setlocal suffixesadd=.md
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'vimwiki'
setlocal syntax=vimwiki
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=./tags,./TAGS,tags,TAGS,~/.tags
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
let s:l = 5 - ((4 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 08|
tabnext 2
set stal=1
badd +1 tp2.py
badd +0 tp2IN_Hategekimana_Fabrice.md
badd +51 ~/note/note_py.md
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
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
