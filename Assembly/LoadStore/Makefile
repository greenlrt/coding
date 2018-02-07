#Makefile
all: load
	./$? ; echo $$?

load: load.o
	gcc -o $@ $?

load.o: load.s
	as -o $@ $<

clean:
	rm -vf load load.o
