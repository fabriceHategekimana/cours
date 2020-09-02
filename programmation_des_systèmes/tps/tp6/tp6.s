
	.data
var:	.word	5
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r0,#7
	ldr	r2,=var
	str	r0,[r2]
	ldr	r1,=var
	ldr	r1,[r1]
	ldr	r0,=num
	bl	printf
	ldmfd	sp!,{lr}
	mov	pc,lr

