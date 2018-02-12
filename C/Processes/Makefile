# Makefile

all: server client

server: server.o
	gcc -pthread server.o -o server

server.o: server.c processes.h
	gcc -c -pthread server.c -o server.o

client: client.o
	gcc -pthread client.o -o client

client.o: client.c processes.h
	gcc -c -pthread client.c -o client.o
