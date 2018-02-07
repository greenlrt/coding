/* Server.c - Starts processes which add to an integer stored in memory */

#include <stdio.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
	if (argc < 3) {
		printf("Please enter 2 arguments");
	}

	pid_t pid;
	int n = 0;
	int i = 0;
	int count = atoi(argv[1]);
	pid_t processes[count];

	while (i < count) {
		pid = fork();
		if (pid < 0) {
			printf("fork failed");
		}
	}
}
