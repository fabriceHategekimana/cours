	.data
strd:	.asciz	" %u "
strx:	.asciz	" %x "
nl:	.asciz	"\n"

length: .byte   0x0A
tab:	.byte   0xFF, 0x0A, 0x00, 0xB0, 0x01, 0xE0, 0xFF, 0xB0, 0x04, 0x50
	
	.align	2

	.text
	.globl	main

main:	stmfd	sp!,{lr}
	ldr	r3,=length
        ldrb    r3,[r3]


	ldr	r0,=strx
	mov	r1,r3
	stmfd	sp!,{r3}	// attention printf peut modifier r0-r3
	bl	printf
    	ldmfd	sp!,{r3}


        cmp     r3,#0
        beq	fin		// tableau vide

	ldr	r0,=nl
	stmfd	sp!,{r3}
	bl	printf
	ldmfd	sp!,{r3}

	mov	r4,#0
	ldr	r5,=tab
        ldr	r0,=strd
1:      ldrb	r1,[r5,r4]	// nombres non signes
	stmfd	sp!,{r0,r3}
	bl	printf	
	ldmfd	sp!,{r0,r3}
	add	r4,r4,#1
	cmp	r4,r3
	bls	1b

	ldr	r0,=nl
	stmfd	sp!,{r3}
	bl	printf
	ldmfd	sp!,{r3}

	mov	r4,#0
	ldr	r5,=tab
        ldr	r0,=strx
1:      ldrb	r1,[r5,r4]	// nombres non signes
	stmfd	sp!,{r0,r3}
	bl	printf	
	ldmfd	sp!,{r0,r3}
	add	r4,r4,#1
	cmp	r4,r3
	bls	1b


	ldr	r0,=nl
	stmfd	sp!,{r3}
	bl	printf
	ldmfd	sp!,{r3}
   

	sub	r5,r3,#1
for1:   cmp     r5,#1		// r5 est i
        blo     fintri
        mov	r6,#0		// r6 est j
	ldr	r4,=tab
for2:	cmp	r6,r5
	bhs     1f
	ldrb	r7,[r4],#1
	add	r6,r6,#1
	ldrb	r8,[r4]
	cmp     r7,r8
	bhs	for2
        strb	r7,[r4]
	strb	r8,[r4,#-1]
	b	for2
1:	sub	r5,r5,#1
	b	for1
	

fintri: ldr	r0,=nl
	stmfd	sp!,{r3}
	bl	printf
	ldmfd	sp!,{r3}

	mov	r4,#0
	ldr	r5,=tab
        ldr	r0,=strd
1:      ldrb	r1,[r5,r4]	// nombres non signes
	stmfd	sp!,{r0,r3}
	bl	printf	
	ldmfd	sp!,{r0,r3}
	add	r4,r4,#1
	cmp	r4,r3
	bls	1b

fin:	ldr	r0,=nl
	stmfd	sp!,{r3}
	bl	printf
	ldmfd	sp!,{r3}

	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr
