#Makefile
all: loadStore
	./$? ; echo $$?

loadStore: loadStore.o
	gcc -o $@ $?

loadStore.o: loadStore.s
	as -o $@ $<

clean:
	rm -vf loadStore loadStore.o
