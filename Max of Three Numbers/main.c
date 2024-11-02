//Write a program to find the max of three numbers using a max function
#include <stdio.h>

int maxNum(int x, int y, int z); //function prototype
int main(void) 
{
int a,b,c;
printf("Enter 3 integers: ");
scanf("%d %d%d", &a,&b,&c);
printf("The max number is %d", maxNum(a,b,c));
  return 0;
}
int maxNum(int x, int y, int z)
{
int maxNumber = x;
if (y>maxNumber)
{
  maxNumber = y;
}
if(z> maxNumber)
{
  maxNumber = z;
}
return maxNumber;
}
