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
	ldr	r0,=tab	 
	ldr	r1,=length
        ldrb    r1,[r1]
	mov	r2,#1
	bl	afftab		// affichage tab avant tri

	ldr	r0,=tab
	ldr	r1,=length
	ldrb	r1,[r1]
	bl	tribu		// tri bulle

	ldr	r0,=tab	 
	ldr	r1,=length
        ldrb    r1,[r1]
	mov	r2,#1
	bl	afftab		// affichage tableau apres


	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr




	//  tribulle
	//  r0: pointeur sur le debut du tableau
	//  r1: nombre d'elements
tribu:  stmfd	sp!,{r4-r6}


	
	sub	r2,r1,#1
1:	cmp     r2,#1		// r2 est i
        blo     4f


        mov	r3,#0		// r3 est j
	mov	r4,r0
2:	cmp	r3,r2
	bhs     3f
	ldrb	r5,[r4],#1
	add	r3,r3,#1
	ldrb	r6,[r4]
	cmp     r5,r6
	bhs	2b
        strb	r5,[r4]
	strb	r6,[r4,#-1]
	b	2b
3:	sub	r2,r2,#1
	b	1b
4:	ldmfd	sp!,{r4-r6}
	mov	pc,lr

	// affichage du tableau en hexadecimal
        // r0: pointeur sur le tableau
        // r1: nombres d'elements
	// r2: ==0 affichage hexa; !=0 affichage decimal

afftab:	stmfd	sp!,{r4-r7,lr}
	mov	r4,r0
	mov	r5,r1
	mov	r7,r2
	ldr	r0,=nl      // new line
	bl	printf	    // attention r0-r3 modifies


	mov	r6,#0
1:      cmp	r7,#0
	ldreq	r0,=strx
	ldrne	r0,=strd
	ldrb	r1,[r4,r6]	// nombres non signes
	bl	printf	
	add	r6,r6,#1
	cmp	r6,r5
	blo	1b
	ldr	r0,=nl      // new line
	bl	printf	    
	ldmfd	sp!,{r4-r7,pc}

