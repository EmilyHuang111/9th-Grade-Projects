/*program to find the sum, the average, the product, the smallest and the largest of three numbers.*/
#include <stdio.h>

int main(void) {
  
int num1 = 0;
int num2 = 0;
int num3 = 0;
int max = 0;
int min = 0;
printf("Enter three different integers: ");
scanf("%d %d %d", &num1,&num2,&num3);
if (num1<=num2)
{min = num1;}
if (num1>num2)
{min = num2;}
if (num3<min)
{min = num3;}
if (num1<=num2)
{max = num2;}
if (num1>num2)
{max = num1;}
if (num3>max)
{max = num3;}  
printf("Sum is %d\n",num1+num2+num3);
printf("Average is %0.2f\n",(num1+num2+num3)/3.0);
printf("Product is %d\n",num1*num2*num3);
printf("Smallest is %d\n",min);
printf("Largest is %d\n",max);
return 0;
}
