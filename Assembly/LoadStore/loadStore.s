/* -- loadStore.s */

/* -- Data section */
.data

.balign 4
myvar1:
	.word 0

/* -- Code section */
.text

/* Ensure code is 4 byte align */
.balign 4
.global main
main:
	ldr r1, addr_of_myvar1	/* r1 <-- &myvar1 */
	mov r2, #3		/* r3 <-- 3 */
	str r2, [r1]		/* *r1 <-- r2 */

	ldr r0, addr_of_myvar1 	/* r0 <-- &myvar1 */
	ldr r0, [r0]		/* r1 <-- *r0 */
	bx lr

/*Labels needed to access data */
addr_of_myvar1 : .word myvar1
