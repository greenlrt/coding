# Makefile

all: loop

loop: loop.o
	gcc -o $@ $?

loop.o: loop.s
	as -o $@ $<

loop.s: loop.c
	gcc -S $^ -o $@

clean:
	rm -vf loop loop.o loop.s
