
COURS=parallelisme
all: task
 
revisions: FORCE
	cd ~/cours/parallelisme/revisions
exercices: FORCE
	cd ~/cours/parallelisme/exercices
tps: FORCE
	cd ~/cours/parallelisme/tps
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

