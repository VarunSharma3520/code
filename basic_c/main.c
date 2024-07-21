#include <stdio.h>


int main()
{

  int a = 4;
  int b = 5;
  int c = a + b;
  int *p = &a;

  // Print the value of c
  printf("%d\n", c);

  // Print the address of a
  printf("address of a: %p\n", (void *)&a);
  printf("address of p: %p\n", &p);

  // Check if a is less than b
  if (a < b) {
    printf("a is less than b\n");
  }

  // Print Hello World
  printf("Hello World!\n");

  return 0;
}
