
	.data
num:	.asciz	" %u "
tab:	.byte	9,8,7,6,5,4,3,2,1,0

	.text
	.globl main

main:	stmfd	sp!,{lr}
	ldr	r0,=num		//on définit le format de sortie a décimal
	ldr	r4,=tab		//on charge la table
	mov	r5,#10		//1er compteur de 10 jusqu'à 0
	mov	r6,#0		//2e compteur à 0 (doit reset à chaque itération du premier)
	mov	r7,#0		//intermédiaire pour l'echange	

bloci:	cmp	r5, #1	
	bmi	end
	subs	r5,r5,#1
	mov	r6,#0
	b	blocj

blocj:	cmp	r5,r6
	beq	bloci
	stmfd	sp!,{r4,r5,r6,r7}
	ldrb	r5,[r4,r6]	//on met dans r5 et r6 T[j] et T[j+1]
	add	r6,r6+1
	ldrb	r6,[r5,r6]
	bl	printf
	ldr	r0,=num		//on définit le format de sortie a décimal
	b	affi

end:	ldmfd	sp!,{lr}
	mov	pc,lr

