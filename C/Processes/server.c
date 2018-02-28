/* Server.c - Starts processes which add to an integer stored in memory */

#include "processes.h"

int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("Please enter 1 arguments.\n");
		return 1;
	}

	pid_t pid;
	key_t key;
	int id;
	char *command;
	struct SharedMemory *shm;
	int i = 0;
	int count = atoi(argv[1]);
	pid_t processes[count];
	char *args[2];
	args[0] = "./client";

	key = 3456;

	id = shmget(key, sizeof(int), IPC_CREAT | 0666);
	sprintf(args[1], "%d", id);

	shm = shmat(id, NULL, 0);
	shm->n = 0;
	sem_init(&(shm->sem), 1, 1);

	while (i < count) {
		pid = fork();
		if (pid < 0) {
			printf("fork failed");
		} else if (pid == 0) {
			/* execute client */
			/*sprintf(command, "./client %d", id);
			system(command);*/
			execvp("./client", args);
			return 0;
		} else {
			processes[i] = pid;
		}
		i++;
	}

	for(i = 0; i < count; i++) {
		waitpid(processes[i], NULL, 0);
	}

	printf("final value: %d\n", shm->n);
	sem_destroy(&(shm->sem));
	shmdt(shm);
	return 0;
}
