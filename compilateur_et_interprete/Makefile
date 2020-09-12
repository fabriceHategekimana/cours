
COURS=compilateur_et_interprete
all: ex1
 
examen: FORCE
	vim ~/cours/compilateur_et_interprete/examen/ExamQuestions.md

revisions: FORCE
	cd ~/cours/compilateur_et_interprete/revisions
exercices: FORCE
	cd ~/cours/compilateur_et_interprete/exercices
tps: FORCE
	cd ~/cours/compilateur_et_interprete/tps
addtask: FORCE
	. ~/sh/mytask.sh
summary: FORCE
	task $(COURS) summary
task: FORCE
	task $(COURS)$(SUB)
note: FORCE
	vim note/note.md
pdf: FORCE
	cd pdf && bash ~/sh/cs.sh

ex1: FORCE
	cd exercice/ex1/ && vim arbre.py
FORCE:

