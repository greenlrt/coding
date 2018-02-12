/* client.c - Adds to variable stored in shared memory */
#include "processes.h"

int main(int argc, char *argv[]) {
	if (argc > 2) {
		printf("Please enter 1 arguments");
	}

	key_t key;
	int id = atoi(argv[1]);
	struct SharedMemory *shm;

	key =3456;

	id = shmget(key, sizeof(int), IPC_EXCL);
	shm = shmat(id, NULL, 0);

	sem_wait(&(shm->sem));
	shm->n = shm->n + 1;

	printf("Added 1 to shared memory\n");
	sem_post(&(shm->sem));
	return 0;
}
