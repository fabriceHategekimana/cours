
	.data
hll:	.asciz	"Hello world"
a:	.word	0x91e6d6a5
m:	.word	0xffffffff
num:	.asciz	" %u "
txt:	.asciz	"Hello world!"
	.text
	.globl main
main:	stmfd	sp!,{lr}
	mov	r0,#5
	mov	r1,#7
	bl	f
	ldr	r1,=m
	bl	mod
	mov	r1,r0
	ldr	r0,=num	
	bl	printf
	b	end


end:	ldmfd	sp!,{lr}
	mov	pc,lr


//---------FONCTION F---------//

f:	stmfd	sp!,{r4-r11}
	ldr	r4,=a
	mla	r0,r4,r0,r4	
	ldmfd	sp!,{r4-r11}
	mov	pc,lr

//---------MODULO---------//

mod:	stmfd	sp!,{r4-r11}
	mov	r3,r1	
plgr:	cmp	r1,r0
	bgt	res
	add	r1,r1,r3
	b	plgr

res:	sub	r1,r1,r3		
	sub	r0,r0,r1
	ldmfd	sp!,{r4-r11}
	mov	pc,lr

	ldr	r0,=num
	bl	printf	
	
