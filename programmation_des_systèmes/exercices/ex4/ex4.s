
	.data
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r0,#3
	mov	r1,#18

	mov	r2,#0	
	mov	r3,#32
b1:	sub	r3,r3,#1
	mov	r4,r1,lsr r3
	b	t1

t1:	cmp	r4,r0
	bpl	b2
	bmi	t2

b2:	sub	r1,r1,r0,lsl r3
	mov	r4,#1
	add	r2,r2,r4,lsl r3
	b	t2

t2:	cmp	r3,#0
	beq	b3
	b	b1

b3:	mov	r1,r2
	ldr	r0,=num
	bl	printf

end:	ldmfd	sp!,{lr}
	mov	pc,lr

