# Makefile

all: transverse

transverse: transverse.o
	gcc -o $@ $?

transverse.o: transverse.s
	as -o $@ $<

transverse.s: transverse.c
	gcc -S $^ -o $@

insertion: insertion.o
	gcc -o $@ $?

insertion.o: insertion.s
	as -o $@ $<

insertion.s: insertion.c
	gcc -S $^ -o $@

deletion: deletion.o
	gcc -o $@ $?

deletion.o: deletion.s
	as -o $@ $<

deletion.s: deletion.c
	gcc -S $^ -o $@

search: search.o
	gcc -o $@ $?

search.o: search.s
	as -o $@ $<

search.s: search.c
	gcc -S $^ -o $@

update: update.o
	gcc -o $@ $?

update.o: update.s
	as -o $@ $<

update.s: update.c
	gcc -S $^ -o $@

clean:
	rm -vf transverse transverse.o transverse.s
	rm -vf insertion insertion.o insertion.s
	rm -vf deletion deletion.o deletion.s
	rm -vf search search.o search.s
	rm -vf update update.o update.s
