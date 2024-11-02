//Program to Print the Decimal Equivalent of a Binary Number 
#include <stdio.h>

int main(void) {
int a, b, c, d, e, n, decimal;
printf("Enter a five digit integer number using 1's and 0's:\n");
scanf("%d", &n);
a  = n % 10;
b = n / 10 % 10;
c = n / 100 % 10;
d = n / 1000 % 10;
e = n / 10000;

if (e==1)
{
  e=16;
  printf("%d ", e);
}
else 
{
  printf("%d ", e);
}
if (d==1)
{
  d=8;
  printf("%d ", d);
}
else
{
  printf("%d ", d);
}
if(c==1) 
{
  c=4;
  printf("%d ", c);
}
else
{
  printf("%d ", c);
}
if(b==1)
{
  b=2;
  printf("%d ", b);
}
else
{
  printf("%d ", b);
}
if(a==1)
{
  a=a*1;
    printf("%d ", a);
}
else
{
  printf("%d ", a);
}
decimal = a + b + c + d + e;
printf("\nThe decimal equivalent of that binary number is: %d\n", decimal);
  return 0;
}
