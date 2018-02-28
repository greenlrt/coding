/* processes.h - Creates shared structure to store semaphores and other shared data */

#include <stdio.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <semaphore.h>
#include <unistd.h>

struct SharedMemory {
	int n;
	sem_t sem;
};
