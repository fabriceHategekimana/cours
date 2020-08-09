
	.data
str1:	.asciz	"%d"
str2:	.asciz	"you entered %d\n"
n:	.word	0
	.text
	.globl main
main:	stmfd	sp!,{lr}
	ldr	r0,=str1	
	ldr	r1,=n	
	bl	scanf
	ldr	r0,=str2
	ldr	r1,=n
	ldr	r1,[r1]
	bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr

