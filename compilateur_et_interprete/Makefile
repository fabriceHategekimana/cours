
COURS=compilateur_et_interprete
all: task
 
revisions: FORCE
	cd ~/cours/compilateur_et_interprete/revisions
exercices: FORCE
	cd ~/cours/compilateur_et_interprete/exercices
tps: FORCE
	cd ~/cours/compilateur_et_interprete/tps
addtask: FORCE
<<<<<<< Updated upstream
	bash ~/sh/mytask.sh +cours
summary: FORCE
=======
	. ~/sh/mytask.sh 
summar: FORCE
>>>>>>> Stashed changes
	task $(COURS) summary
task: FORCE
	task $(COURS)$(SUB)
note: FORCE
	vim note/note.md
pdf: FORCE
	cd pdf && bash ~/sh/cs.sh
FORCE:

