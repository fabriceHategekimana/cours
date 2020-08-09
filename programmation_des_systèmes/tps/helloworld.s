	.data
str:	.asciz	"Hello World\n"
nb:	.word	7

	.text
	.globl	main

main:	stmfd	sp!,{lr}
	ldr	r0,=str
	bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr

