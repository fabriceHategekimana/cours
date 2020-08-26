
	.data
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}

	ldmfd	sp!,{lr}
	mov	pc,lr

