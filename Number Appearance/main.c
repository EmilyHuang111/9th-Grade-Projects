#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
 srand(time(0));
  int z[100];
  int count;
  int number;
  
  for (int y = 0; y <= 99; y++) {
    z[y] = rand() % 101;
  }
  for (int y = 1; y <= 100; y++) {
    printf("%d\t", z[y - 1]);
    if (y % 20 == 0) {
      printf("\n");
    }
  }
printf("Enter a number between 0 and 100: ");
scanf("%d", &number);
  for(int y=0; y <= 99; y++)
    {
      if (z[y] == number)
      {
        count++;
      }
    }
  printf("The number %d appears %d time(s)", number, count);
  return 0;
}
