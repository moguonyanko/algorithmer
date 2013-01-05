#include <stdio.h>
#include <assert.h>
#import <Foundation/Foundation.h>>

NSArray thePouring(NSArray *capacities, NSArray *bottles, 
		NSArray *fromId, NSArray *toId)
{
	int size = [fromId count];
	for(int i = 0; i < size; i++){
		int f = [fromId objectAtIndex:i];
		int t = [toId objectAtIndex:i];
		int space = [capacities objectAtIndex:t] - [bottles objectAtIndex:t];

		if(space >= [bottles objectAtIndex:f]){
			int vol = [bottles objectAtIndex:f];
			[bottles objectAtIndex:t] += vol;
			[bottles objectAtIndex:f] = 0;
		}else{
			int vol = space;
			[bottles objectAtIndex:t] += vol;
			[bottles objectAtIndex:f] -= vol;
		}
	}

	return bottles;
}

int main(int argc, const char * argv[])
{
	@autoreleasepool{
		NSArray *capacities = [NSArray arrayWithObjects:30, 20, 10];
		NSArray *bottles = [NSArray arrayWithObjects:10, 5, 5];
		NSArray *frimId = [NSArray arrayWithObjects:0, 1, 2];
		NSArray *toId = [NSArray arrayWithObjects:1, 2, 0];
		NSArray *check = [NSArray arrayWithObjects:10, 10, 0];

		NSArray *result = thePouring(capacities, bottles, fromId, toId);

		for(int i = 0, limit = [result count]; i < limit; i++){
			printf("%d\n", [result objectAtIndex:i]);
			assert([result objectAtIndex:i] == [check objectAtIndex:i]);
		}

		printf("OK\n");
	}

	return 0;
}

