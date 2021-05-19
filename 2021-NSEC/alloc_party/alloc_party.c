#include <stdio.h>
#include <stdlib.h>

/*
 * So we have a situation where the malloc’s argument contains an arithmetic operation
 * This can lead to two cases:
 *  1. Zero Allocation (if the operation makes the argument 0 we get a NULL ptr)
 *  2. Overflow, if the computed allocation is smaller and we use memcpy() eventually
 */

void *alloc_havoc(int y) {
  int z = 10;
  void *x = malloc(y * z);
  return x;
}

/*
 * Double free on same mem chunks can be quite dangerous when there are allocations 
 * in between. It is possible that mem allocators recycle the pointers leading to an
 * accidental/unintended free and hence subsequent chances of getting b0rked!
 */

void double_trouble(char* p, char* q) {
    p = malloc(10);   // 0x40013 address assigned on heap
    free(p);                // free up 0x40013 chunk
    q = malloc(10); // 0x40013 probably reassigned
    free(p); // Double Free!! If we use *q now...
    int val = atoi(p); // Use after free
}
