
COURS=imagerie_numerique
all: task
 
revisions: FORCE
	cd ~/cours/imagerie_numerique/revisions
exercices: FORCE
	cd ~/cours/imagerie_numerique/exercices
tps: FORCE
	cd ~/cours/imagerie_numerique/tps
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

