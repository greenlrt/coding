# Makefile
all: first

first: first.o
	gcc -0 $@ $+

first.o : first.s
	gcc -0 $@ $<

clean:
	rm -vf first *.o
