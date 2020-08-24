
	.data
num:	.asciz	" %u "
tab:	.byte	9,8,7,6,5,4,3,2,1,0

	.text
	.globl main

main:	stmfd	sp!,{lr}
	ldr	r0,=num		//on définit le format de sortie a décimal
	mov	r5,#10		//on définit notre compteur à 10 jusqu'à 0
	ldr	r4,=tab		//on charge la table

affi:	cmp	r5, #1	
	bmi	end
	subs	r5,r5,#1
	ldrb	r1,[r4,r5]
	bl	printf
	ldr	r0,=num		//on définit le format de sortie a décimal
	b	affi

end:	ldmfd	sp!,{lr}
	mov	pc,lr

