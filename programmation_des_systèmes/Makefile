COURS=project:programmation_des_systèmes

all: start
 
start:
	echo hello world!
revisions:
	cd ~/cours/revisions
exercices:
	cd ~/cours/exercices
tps:
	cd ~/cours/tps
addtask: FORCE
	bash ~/sh/mytask.sh
summary: FORCE
	task $(COURS) summary
task: FORCE
	task $(COURS)$(SUB)
project: FORCE
	echo "$(COURS)"
note: FORCE
	vim note/note.md
pdf: FORCE
	cd pdf && bash ~/sh/cs.sh
FORCE:
