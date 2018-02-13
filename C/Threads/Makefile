# Makefile

all: threads

threads: threads.o
	gcc -pthread threads.o -o threads

threads.o: threads.c
	gcc -c -pthread threads.c -o threads.o
