
	.data
rep:	.asciz	"On change le signe de r0"
a:	.word	9
b:	.word	3
max:	.word	0xFFFFFFFF
num:	.asciz	" u "
num2:	.asciz	" %i "
hex:	.asciz	" 0x%x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	ldr	r0,=a
	ldr	r0,[r0]
	ldr	r1,=b
	ldr	r1,[r1]
	bl	unsdiv
		
	mov	r1,r0
	ldr	r0,=num2
	bl	printf

fin:	ldmfd	sp!,{lr}
	mov	pc,lr

//----------unsdiv----------//
sigdiv:	stmfd	sp!,{r4-r11}
		
init2:	mov	r4,#1		//on commence avec l'assertion que le future résutlat est positif
	mov	r2,r0,lsr #31	
	cmp	r2,#1
	beq	pos0

suite:	mov	r2,r1,lsr #31
	cmp	r2,#1
	beq	pos1
	b	suite2

pos0:	rsb	r4,#1		//on change le signe du future résultat
	ldr	r2,=max		//on rend r0 positif
	ldr	r2,[r2]
	sub	r0,r2,r0
	add	r0,r0,#1
	b	suite

pos1:	rsb	r4,#1		//on change le signe du future résultat
	ldr	r2,=max		//on rend r1 positif
	ldr	r2,[r2]
	sub	r1,r2,r1
	add	r1,r1,#1
	b	suite2

suite2:	mov	r2,r1
	mov	r3,r0
	mov	r0,#1	

test2:	cmp	r3,r2
	bmi	adju2
	beq	ptest
	b	loop2

loop2:	add	r0,r0,#1
	add	r2,r2,r1
	b	test2

adju2:	cmp	r0,#1	
	subpl	r0,r0,#1
ptest:	cmp	r4,#1		//on vérifie si on doit changer le signe du résultat actuel
	bne	pos2
	b	end2

pos2:	ldr	r2,=max		//on rend r0 positif
	ldr	r2,[r2]
	sub	r0,r2,r0
	add	r0,r0,#1

end2:	ldmfd	sp!,{r4-r11}
	mov	pc,lr

//----------unsdiv----------//
unsdiv:	stmfd	sp!,{r4-r11}
		
init:	mov	r2,r1
	mov	r3,r0
	mov	r0,#1	

test:	cmp	r3,r2
	bmi	adju
	beq	end	
	b	loop

loop:	add	r0,r0,#1
	add	r2,r2,r1
	b	test

adju:	cmp	r0,#1	
	subpl	r0,r0,#1

end:	ldmfd	sp!,{r4-r11}
	mov	pc,lr
