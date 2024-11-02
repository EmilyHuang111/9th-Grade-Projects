/*Using if statements, relational operators, and equality operators.*/
#include <stdio.h>

int main(void) 
{

 int num1 = 0;
 int num2 = 0;
  printf("Enter two integers, and I will tell you \n");
  printf("the relationship they satify: ");
  scanf("%d %d",&num1,&num2);

  if (num1 > num2)
  {
     printf("%d is greater than %d\n",num1,num2);
  }
  if (num1 < num2)
  {
  printf("%d is less than %d\n",num1,num2);
  }
  if (num1 == num2)
  {
     printf("%d is equal to %d\n", num1,num2);
  }
  
  return 0;
}
