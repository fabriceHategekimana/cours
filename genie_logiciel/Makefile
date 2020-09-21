
COURS=genie_logiciel
all: task
 
revisions: FORCE
	cd ~/cours/genie_logiciel/revisions
exercices: FORCE
	cd ~/cours/genie_logiciel/exercices
tps: FORCE
	cd ~/cours/genie_logiciel/tps
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

