/* threads.c - Starts multiple threads that add to global variable */

#include <stdio.h>
#include <pthread.h>

void *add();

int n;

int main(int argc, char *argv[]) {
	if (argc > 2) {
		printf("Please enter 2 arguments.");
	}

	int count = atoi(argv[1]);
	pthread_t tid[count];
	int i;

	n = 0;

	for(i = 0; i < count; i++) {
		pthread_create(&tid[i], NULL, add, NULL);
	}

	for(i = 0; i < count; i++) {
		pthread_join(tid[i], NULL);
	}

	printf("final value: %d\n", n);

	return 0;
}

void *add() {
	n = n + 1;
	printf("Added 1 to n\n");
}
