/* threads.c - Starts multiple threads that add to global variable */

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

void *add();

sem_t s;
int n;

int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("Please enter 2 arguments.\n");
		return 1;
	}

	int count = atoi(argv[1]);
	pthread_t tid[count];
	int i;

	n = 0;
	sem_init(&s, 0, 1);

	for(i = 0; i < count; i++) {
		pthread_create(&tid[i], NULL, add, NULL);
	}

	for(i = 0; i < count; i++) {
		pthread_join(tid[i], NULL);
	}

	printf("final value: %d\n", n);
	sem_destroy(&s);
	return 0;
}

void *add() {
	sem_wait(&s);
	n = n + 1;
	printf("Added 1 to n\n");
	sem_post(&s);
}
