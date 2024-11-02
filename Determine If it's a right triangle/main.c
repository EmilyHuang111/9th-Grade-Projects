//Program to determine if a right triangle
#include <stdio.h>
int main(void) {
int x, y, z;
printf("Type Three Integers:  ");
scanf("%d%d%d", &x, &y, &z);
if (x*x + y*y == z*z)
{
printf("These lengths represent a right triangle");
}
else if ( x*x + z*z == y*y)
{
printf("These lengths represent a right triangle");
}
else if (y*y + z*z == x*x)
{
printf("These lengths represent a right triangle");
}
else 
{printf("These lengths don't represent a right triangle");}
  
return 0;
}
