/*Class average program with sentinel-controlled iteration*/
#include <stdio.h>

int main(void) {
#include <stdio.h>

 int number, sum=0, count=0;
  printf("%s", "Enter a grade, type -1 to end: ");
  scanf("%d", &number);
  
  while(number != -1)
    {
     sum += number;
     count++; 
     printf("%s", "Enter a grade, type -1 to end: ");
     scanf("%d", &number);
    }
  if (count !=0)
  {
    double average = (double)sum/count; //Cast sum to a double
    printf("The average is: %.2f ", average);
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
  
  }
  else
  {
   puts("No grades were entered"); //puts can't have %d's or %f's
  }

  return 0;
}
