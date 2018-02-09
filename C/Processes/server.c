/* Server.c - Starts processes which add to an integer stored in memory */

#include <stdio.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if (argc < 3) {
		printf("Please enter 2 arguments");
	}

	pid_t pid;
	key_t key;
	int id;
	char *command;
	int *shm = 0;
	int i = 0;
	int count = atoi(argv[1]);
	pid_t processes[count];

	key = 1234;

	if ((id = shmget(key, sizeof(int), IPC_CREAT | IPC_EXCL)) < 0) {
		perror("shmget");
		exit(1);
	}

	shm = shmat(id, NULL, 0);
	*shm = 0;

	while (i < count) {
		pid = fork();
		if (pid < 0) {
			printf("fork failed");
		} else if (pid == 0) {
			/* execute client */
			sprintf(command, "./client %d", id);
			system(command);
		} else {
			processes[i] = pid;
			break;
		}
		i++;
	}

	for(i = 0; i < count; i++) {
		waitpid(processes[i], NULL, WNOHANG);
	}

	printf("%d", *shm);
	shmdt(shm);
	return 0;
}
