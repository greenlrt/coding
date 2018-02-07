#Makefile
all: multiply

multiply: $@.o
	gcc -o $@ $+
	./$@ ; echo $$?

multiply.o: $@.s
	as -o $@ $<

clean:
	rm -vf multiply multiply.o
