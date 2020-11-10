all:exemple

compile: FORCE
	gcc tp4.c -o lock

exemple: compile
	./lock teste.txt	

clean: FORCE
	rm lock TP4SI_Hategekimana_Fabrice.zip

zip:
	zip TP4SI_Hategekimana_Fabrice lock.c Makefile teste.txt TP4SI_Hategekimana_Fabrice.pdf
FORCE:

