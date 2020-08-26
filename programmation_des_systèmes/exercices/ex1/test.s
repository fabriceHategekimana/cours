
	.data
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r1,#0
	mov	r2,#1
	add	r1,r1,r2,ASL #2
	ldr	r0,=num
	bl	printf
	ldmfd	sp!,{lr}
	mov	pc,lr

