//Addition Program
#include <stdio.h>

int main(void) 
{
  int integer1=0;
  int integer2=0;
  
 printf("Enter first nmber: ");
 scanf("%d",&integer1);

 printf("Enter second nmber: ");
 scanf("%d",&integer2);

   printf("Enter two numbers: ");
   scanf("%d%d",&integer1,&integer2);
  
 int sum = integer1 + integer2;


   printf("The sum of %d and %d is %d" ,integer1,integer2, integer1+integer2);
  
  return 0;
}
