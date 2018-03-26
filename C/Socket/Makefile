# Makefile

all: client

client: client.o
	gcc client.o -o client

client.o: client.c socket.h
	gcc -c -g client.c -o client.o
