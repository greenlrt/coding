/* -- multiply.s */
.global main

main:
	mov r0, #2	/* r0 <-- 2 */
	mov r1, #3	/* r1 <-- 3 */
	mul r0, r0, r1	/* r0 <-- r0 * r1 */
	bx lr

