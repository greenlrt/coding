/* -- load.s */

/* -- Data section */
.data

.balign 4
myvar1:
	.word 3

/* -- Code section */
.text

/* Ensure code is 4 byte align */
.balign 4
.global main
main:
	ldr r1, addr_of_myvar1 /* r1 <-- &myvar1 */
	ldr r1, [r1]	/* r1 <-- *r1 */
	bx lr

/*Labels needed to access data */
addr_of_myvar1 : .word myvar1
