/* -- branch01.s */
.text
.global main
main:
	mov r0, #1 /* r0 <-- 1 */
	b end	   /* branch to 'end' */
	mov r0, #0 /* r0 <-- 0 */
end:
	bx lr
