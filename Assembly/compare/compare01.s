/* -- compare01.s */
.text
.global main
main:
	mov r1, #1	/* r1 <-- 1 */
	mov r2, #1	/* r2 <-- 1 */
	cmp r1, r2	/* compare r1 and r2 */
	beq case_same	/* branch if Z = 1 */
case_different:
	mov r0, #0	/* r0 <-- 0 */
	b end		/* branch to end */
case_same:
	mov r0, #1	/* r0 <-- 1 */
end:
	bx lr
