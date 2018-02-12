/* client.c - Adds to variable stored in shared memory */
#include <stdio.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if (argc > 2) {
		printf("Please enter 1 arguments");
	}

	key_t key;
	int id = atoi(argv[1]);
	int *shm;

	key =3456;

	id = shmget(key, sizeof(int), IPC_EXCL);
	shm = shmat(id, NULL, 0);
	*shm = *shm + 1;

	printf("Added 1 to shared memory\n");
	return 0;
}
