
	.data
num:	.asciz	" %u "
hex:	.asciz	" %x "
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r0,#5
	bl	fact
    	mov	r1,r0	
	ldr	r0,=num
	bl	printf	
	ldmfd	sp!,{lr}
	mov	pc,lr


//----------factorielle----------//
fact:	stmfd	sp!,{r4-r11}

init:	mov	r1,r0	

loop:	sub	r1,r1,#1
	mov	r2,r0
	mul	r0,r2,r1

test:	cmp	r1,#1
	beq	end
	b	loop

end:	ldmfd	sp!,{r4-r11}
	mov	pc,lr


