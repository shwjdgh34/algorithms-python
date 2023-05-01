/**
 * water.c
 * -------
 * A simple deadlock example. This version will quickly get stuck when all
 * the oxygen wait for hydrogen to get ready at the same time the hydrogen
 * is waiting for the oxygen to get ready. A simple change in order of
 * signal would solve this problem.
 */
#include "thread_107.h"
#define NUM_WATER 10
void main(int argc, char **argv)
{
int i;
bool verbose = (argc == 2 && (strcmp(argv[1], "-v") == 0));
Semaphore oxygenReady, hydrogenReady; // semaphores used as counters
InitThreadPackage(verbose);
oxygenReady = SemaphoreNew("Oxygen Ready", 0);
hydrogenReady = SemaphoreNew("Hydrogen Ready", 0);
13
for (i = 0; i < NUM_WATER; i++)
ThreadNew(“Oxygen”, Oxygen, 2, oxygenReady, hydrogenReady);
for (i = 0; i < 2 * NUM_WATER; i++)
ThreadNew(“Hydrogen”, Hydrogen, 2, oxygenReady, hydrogenReady);
RunAllThreads();
printf("All done!\n");
SemaphoreFree(oxygenReady);
SemaphoreFree(hydrogenReady);
}
static void Hydrogen(Semaphore oxygenReady, Semaphore hydrogenReady)
{
SemaphoreWait(oxygenReady);
SemaphoreSignal(hydrogenReady);
}
static void Oxygen(Semaphore oxygenReady, Semaphore hydrogenReady)
{
SemaphoreWait(hydrogenReady);
SemaphoreWait(hydrogenReady);
SemaphoreSignal(oxygenReady);
SemaphoreSignal(oxygenReady);
printf("Water made!\n");
}