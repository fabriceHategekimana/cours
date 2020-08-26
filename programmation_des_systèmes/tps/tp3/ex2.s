
	.data
num:	.asciz	" %u "
txt5:	.asciz	"r5="
txt6:	.asciz	"r6="
tab:	.byte	9,8,7,6,5,4,3,2,1,0

	.text
	.globl main

main:	stmfd	sp!,{lr}
	ldr	r0,=num		//on définit le format de sortie a décimal
	ldr	r4,=tab		//on charge la table r4= T
	mov	r5,#10		//1er compteur i de 2 jusqu'à 0
	mov	r6,#0		//2e compteur j à 0 (doit reset à chaque itération du premier)
	mov	r7,#0		//intermédiaire pour l'echange	

bloci:	subs	r5,r5,#1	//else{ r5--
	beq	aff		//	aff() }
	mov	r6,#0		//	r6= 0
	b	blocj		//	blocj()}
	
blocj:	stmfd	sp!,{r5,r6}	//else{
	mov	r7,r6		//	r7= r6
	ldrb	r5,[r4,r7]	//	r5= T[r7] 
	add	r7,r7,#1	// pour le r7+1
	ldrb	r6,[r4,r7]	//r6= T[r7+1]
	cmp	r6,r5		//if (r6 < r5){ //si c'est pas ordonné
	bmi	echa		//	echa
	b	inc

inc:	ldmfd	sp!,{r5,r6}	//else{  recharge des valeurs
	add	r6,r6,#1	//	r6++
	cmp	r5,r6		//if(r5 == r6){
	beq	bloci		//	bloci()
	b	blocj		//	blocj()}

echa:	strb	r5,[r4,r7]	//on enregistre T[j+1]= T[j]
	sub	r7,r7,#1
	strb	r6,[r4,r7]	//on enregistre T[j+1]= T[j]
	b	inc

	
aff:	mov	r5,#0		//on définit notre compteur à 2 jusqu'à 0

affi:	cmp	r5, #10	
	beq	end
	ldrb	r1,[r4,r5]
	bl	printf
	ldr	r0,=num		//on définit le format de sortie a décimal
	add	r5,r5,#1
	b	affi

pri5:	ldr	r0,=txt5
	bl	printf
	mov	r1,r5	
	ldr	r0,=num		//on définit le format de sortie a décimal
	bl	printf	

pri6:	ldr	r0,=txt6
	bl	printf
	mov	r1,r6	
	ldr	r0,=num		//on définit le format de sortie a décimal
	bl	printf	

end:	ldmfd	sp!,{lr}
	mov	pc,lr

