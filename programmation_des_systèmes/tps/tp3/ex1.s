
	.data
str:	.asciz	"Hello world"

	.text
	.globl main

main:	stmfd	sp!,{lr}
	ldr	r0,=str
	bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr

