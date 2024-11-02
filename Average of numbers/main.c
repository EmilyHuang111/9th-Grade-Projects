/* Program to ask the usar to enter the unknown number of grades and the average.*/
#include <stdio.h>
int main(void) {
  int grade,count,sum; 
  count = 0; sum = 0; 
  printf("Enter the integers: \n");
  printf("(Enter -1 after inputing all the desired integers)\n");
  while (scanf("%d",&grade)>-1) 
 {count++; sum += grade; 
 if(grade == -1) {break;}
 }
 double average = (sum + 1.0)/(count-1.0);
 printf("The average is: %.02f", average);
  return 0;
}
