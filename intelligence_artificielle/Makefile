
COURS=intelligence_artificielle
all: actu

actu: FORCE
	cd tps/1/
revisions: FORCE
	cd ~/cours/intelligence_artificielle/revisions
exercices: FORCE
	cd ~/cours/intelligence_artificielle/exercices
tps: FORCE
	cd ~/cours/intelligence_artificielle/tps
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

