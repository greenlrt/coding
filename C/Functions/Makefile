CC = gcc
CFLAGS = -g -ansi

functions: functions.o hello.o factorial.o
	$(CC) $(CFLAGS) $? -o $@

functions.o: functions.c functions.h
	$(CC) -c functions.c

hello.o: hello.c functions.h
	$(CC) -c hello.c

factorial.o: factorial.c functions.h
	$(CC) -c factorial.c
