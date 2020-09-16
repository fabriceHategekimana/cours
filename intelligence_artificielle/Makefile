
COURS=project:IA
all: task
 
revisions: FORCE
	cd ~/cours//revisions
exercices: FORCE
	cd ~/cours//exercices
tps: FORCE
	cd ~/cours//tps
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
FORCE:

