all: start

start: pdf
	vim -S Session.vim
pdf: FORCE
	zathura *.pdf &
zip: FORCE
	zip tp2IN_Hategekimana_Fabrice *.py tp2.pdf
FORCE:
