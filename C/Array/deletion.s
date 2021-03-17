	.arch armv6
	.eabi_attribute 27, 3
	.eabi_attribute 28, 1
	.fpu vfp
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"deletion.c"
	.section	.rodata
	.align	2
.LC1:
	.ascii	"The original array elements are :\000"
	.align	2
.LC2:
	.ascii	"LA[%d] = %d \012\000"
	.align	2
.LC3:
	.ascii	"The array elements after deletion :\000"
	.align	2
.LC0:
	.word	1
	.word	3
	.word	5
	.word	7
	.word	8
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 48
	@ frame_needed = 1, uses_anonymous_args = 0
	stmfd	sp!, {fp, lr}
	add	fp, sp, #4
	sub	sp, sp, #48
	str	r0, [fp, #-48]
	str	r1, [fp, #-52]
	ldr	r3, .L9
	sub	ip, fp, #40
	mov	lr, r3
	ldmia	lr!, {r0, r1, r2, r3}
	stmia	ip!, {r0, r1, r2, r3}
	ldr	r3, [lr]
	str	r3, [ip]
	mov	r3, #3
	str	r3, [fp, #-16]
	mov	r3, #5
	str	r3, [fp, #-20]
	ldr	r0, .L9+4
	bl	puts
	mov	r3, #0
	str	r3, [fp, #-8]
	b	.L2
.L3:
	ldr	r3, [fp, #-8]
	mov	r3, r3, asl #2
	sub	r2, fp, #4
	add	r3, r2, r3
	ldr	r3, [r3, #-36]
	ldr	r0, .L9+8
	ldr	r1, [fp, #-8]
	mov	r2, r3
	bl	printf
	ldr	r3, [fp, #-8]
	add	r3, r3, #1
	str	r3, [fp, #-8]
.L2:
	ldr	r2, [fp, #-8]
	ldr	r3, [fp, #-20]
	cmp	r2, r3
	blt	.L3
	ldr	r3, [fp, #-16]
	str	r3, [fp, #-12]
	b	.L4
.L5:
	ldr	r3, [fp, #-12]
	sub	r1, r3, #1
	ldr	r3, [fp, #-12]
	mov	r3, r3, asl #2
	sub	r2, fp, #4
	add	r3, r2, r3
	ldr	r2, [r3, #-36]
	mov	r3, r1, asl #2
	sub	r1, fp, #4
	add	r3, r1, r3
	str	r2, [r3, #-36]
	ldr	r3, [fp, #-12]
	add	r3, r3, #1
	str	r3, [fp, #-12]
.L4:
	ldr	r2, [fp, #-12]
	ldr	r3, [fp, #-20]
	cmp	r2, r3
	blt	.L5
	ldr	r3, [fp, #-20]
	sub	r3, r3, #1
	str	r3, [fp, #-20]
	ldr	r0, .L9+12
	bl	puts
	mov	r3, #0
	str	r3, [fp, #-8]
	b	.L6
.L7:
	ldr	r3, [fp, #-8]
	mov	r3, r3, asl #2
	sub	r2, fp, #4
	add	r3, r2, r3
	ldr	r3, [r3, #-36]
	ldr	r0, .L9+8
	ldr	r1, [fp, #-8]
	mov	r2, r3
	bl	printf
	ldr	r3, [fp, #-8]
	add	r3, r3, #1
	str	r3, [fp, #-8]
.L6:
	ldr	r2, [fp, #-8]
	ldr	r3, [fp, #-20]
	cmp	r2, r3
	blt	.L7
	mov	r3, #0
	mov	r0, r3
	sub	sp, fp, #4
	@ sp needed
	ldmfd	sp!, {fp, pc}
.L10:
	.align	2
.L9:
	.word	.LC0
	.word	.LC1
	.word	.LC2
	.word	.LC3
	.size	main, .-main
	.ident	"GCC: (Raspbian 4.9.2-10+deb8u2) 4.9.2"
	.section	.note.GNU-stack,"",%progbits
