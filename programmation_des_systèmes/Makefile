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
	task add $(ARGS) $(COURS)$(SUB)
summary: FORCE
	task $(COURS) summary
task: FORCE
	task $(COURS)$(SUB)
project: FORCE
	echo "$(COURS)"
FORCE:
