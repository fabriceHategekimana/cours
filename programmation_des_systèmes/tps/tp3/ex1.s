
	.data
tab:	.byte	1,2,3,4,5,6,7,8,9,0

	.text
	.globl main

main:	stmfd	sp!,{lr}
	ldr	r0,=tab
	bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr

