
COURS=reseaux_informatiques
all: task
 
revisions: FORCE
	cd ~/cours/reseaux_informatiques/revisions
exercices: FORCE
	cd ~/cours/reseaux_informatiques/exercices
tps: FORCE
	cd ~/cours/reseaux_informatiques/tps
addtask: FORCE
	bash ~/sh/mytask.sh +cours
summary: FORCE
	task $(COURS) summary
task: FORCE
	task $(COURS)$(SUB)
note: FORCE
	vim note/note.md
pdf: FORCE
	cd pdf && bash ~/sh/cs.sh
FORCE:

