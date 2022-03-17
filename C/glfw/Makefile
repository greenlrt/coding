CC = g++
CFLAGS = -pthread -lglfw -lGLU -lGL -lXrandr -lXi -lXinerama -lX11 -lrt -ldl

test: test.c
	$(CC) $(CFLAGS) $? -o $@
