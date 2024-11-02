/*This program is for determining even or odd numbers.*/
#include <stdio.h>

int main(void) {
  int num1 = 0;
  printf("Enter one integer, and I will tell you if the number is even or odd: ");
  scanf("%d",&num1 );
  
  if (num1 % 2 == 0)
  {printf("%d is an even number.\n", num1);}
  if (num1 % 2 != 0)
    {printf("%d is an odd number.\n", num1);}
  return 0;
}
