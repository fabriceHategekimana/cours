
	.data
	.text
	.globl main
main:	stmfd	sp!,{lr}

	ldmfd	sp!,{lr}
	mov	pc,lr

