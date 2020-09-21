
COURS=concurrence
all: task
 
revisions: FORCE
	cd ~/cours/concurrence/revisions
exercices: FORCE
	cd ~/cours/concurrence/exercices
tps: FORCE
	cd ~/cours/concurrence/tps
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

