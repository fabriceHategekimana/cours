
	.data
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r0,#7
	mov	r1,#20

b1:	mov	r2,#0
t1:	cmp	r0,#0
	beq	prt	//si c'est nul
	bne	b2	//si c'est pas nul

b2:	mov	r3,r0,lsl #31	//teste de parité
	movs	r3,r3,lsr #31
	bne	b3		//si c'est == 1 (impair)
	beq	b4		//si c'est == 0 (pair)

b3:	add	r2,r2,r1
	b	b4

b4:	mov	r0,r0,lsr #1	//division par 2	
	mov	r1,r1,lsl #1	//multiplication par 2
	b	t1

prt:	mov	r1,r2	
	ldr	r0,=num
	bl	printf
end:	ldmfd	sp!,{lr}
	mov	pc,lr

