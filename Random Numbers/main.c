#include <stdio.h>
#include<stdlib.h>
#include <time.h>
int main(void) 
{
  int num,num2,num3,num4;
  srand(time(0));
for(int x=0; x<=4; x++)
  {
    num = rand();//rand num between 0 - (2^31) -1
    num2 = rand()%10; //rand num between 0-9
    num3 = rand()%10+1; //rand num between 1-10
    num4 = (rand()%10+1)+50; //rand num between 50=60
    printf("%d\t%d\t%d\t%d\n", num, num2, num3, num4);
  }
  return 0;
}
