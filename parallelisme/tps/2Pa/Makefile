all: run

run: src/tp2.cpp src/Array2D.hpp src/Point.hpp
	mpiCC src/tp2.cpp -o laplace -std=c++11 

clean: FORCE
	rm Session.vim log.txt chaleur.dat

pdf: FORCE
	zathura *.pdf &

session: pdf
	vim -S Session.vim

FORCE:
	
