CC = gcc
CFLAGS = -g -ansi

sum: sum.o
	$(CC) $(CFLAGS) $? -o $@

sum.o: sum.c
	$(CC) -c sum.c
