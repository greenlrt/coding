#Makefile
all: multiply
	./$? ; echo $$?

multiply: multiply.o
	gcc -o $@ $?

multiply.o: multiply.s
	as -o $@ $<

clean:
	rm -vf multiply multiply.o
