	.data
invite:	.asciz	"entrez un nombre: "
str:	.asciz	"%d"
nl:	.asciz	"\n"	
val:	.word	0x00

	.text
	.globl	main

main:	stmfd	sp!,{lr}
	ldr	r0,=invite
	bl	printf
	ldr	r0,=str
	ldr	r1,=val
	bl	scanf
	ldr	r0,=val
	ldr	r0,[r0]
	bl	x

	mov	r1,r0
	stmfd	sp!,{r1}
	ldr	r0,=nl      //commentaire
        bl	printf
	ldmfd	sp!,{r1}
	ldr	r0,=str      //commentaire
        bl	printf
	ldr	r0,=nl      //commentaire
        bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr


x:	stmfd	sp!,{r0,r1,lr}
	cmp	r0,#1
	movls	r0,#1
	addls	sp,sp,#4
	ldmlsfd	sp!,{r1,pc}
	sub	r0,r0,#1
	bl	x
	ldr	r1,[sp],#4
	mul	r0,r1,r0
	ldmfd	sp!,{r1,pc}
