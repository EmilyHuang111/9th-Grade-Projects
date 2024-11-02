//Find the average of 10 integers
#include <stdio.h>

int main(void) 
{
 int number, sum=0, count=0;
  while(count<10)
    {
     printf("Enter an integer: ");
     scanf("%d", &number);
     sum += number;      //sum = number + sum;
     count++;           //count = count +1;
    }
  double average = sum/10.0;
  printf("The average is: %.02f ", average);
  if(average >=90)
  {
    puts("A");
  }
  else if (average>=80)
  {
    puts("B");
  }
  else if (average>=70)
  {
    puts("C");
  }
  else if (average>=60)
  {
    puts("D");
  }
  else 
  {
    puts("F");
  }
  
  return 0;
}
