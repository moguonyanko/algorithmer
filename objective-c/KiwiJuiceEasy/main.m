#include <stdio.h>
#include <assert.h>

int len(int array[])
{
	return sizeof(array) / sizeof(array[0]);
}

typedef struct {
	int *bottles;
} Bottle;

Bottle thePouring(int capacities[], int bottles[], 
		int fromId[], int toId[])
{
	int size = len(fromId);
	for(int i = 0; i < size; i++){
		int f = fromId[i];
		int t = toId[i];
		int space = capacities[t] - bottles[t];

		if(space >= bottles[f]){
			int vol = bottles[f];
			bottles[t] += vol;
			bottles[f] = 0;
		}else{
			int vol = space;
			bottles[t] += vol;
			bottles[f] -= vol;
		}
	}

	Bottle b;
	b.bottles = bottles;

	return b;
}

int main(int argc, const char * argv[])
{
	int capacities[] = {30, 20, 10};
	int bottles[] = {10, 5, 5};
	int fromId[] = {0, 1, 2};
	int toId[] = {1, 2, 0};
	int check[] = {10, 10, 0};
	
	Bottle b = thePouring(capacities, bottles, fromId, toId);

	for(int i = 0, limit = len(bottles); i < limit; i++){
		printf("%d\n", b.bottles[i]);
		assert(b.bottles[i] == check[i]);
	}

	printf("OK\n");

	return 0;
}

