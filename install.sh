sudo apt install gcc-arm-linux-gnueabi
sudo apt install qemu-user

echo "
function RunARM()
	let @o= system(\"arm-linux-gnueabi-gcc \".bufname('%').\"&& qemu-arm -L /usr/arm-linux-gnueabi a.out\") 
	echo @o
endfunction

function ARM()
	nnoremap <buffer> <F5> :call RunARM()<CR>
	nnoremap <buffer> <F2> :call Note(\"s\")<CR>
endfunction

autocmd BufReadPre,BufNewFile *.s call ARM()
" >> ~/.vimrc
