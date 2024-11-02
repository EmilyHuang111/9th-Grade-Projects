/*A program the reads three nonzero integer values and prints if it represents the sides of a triangle*/
#include <stdio.h>
int main(void) {
  int integer1, integer2, integer3;
  printf("Enter three numbers: ");
  scanf("%d%d%d",&integer1, &integer2, &integer3);
  if (integer1 >0 && integer2 >0 && integer3 >0){
    if (integer1+integer2>integer3 && integer1-integer2<integer3 && integer2-integer1<integer3){
      if (integer2+integer3>integer1 && integer2- integer3<integer1 && integer3- integer2<integer1){
        if (integer1+integer3>integer2 && integer1-integer3<integer1 && integer3-integer1<integer2){
         printf("This represents the sides of a triangle"); 
         }else {
          printf("This doesn't represent the sides of a triangle");}
       }else{
        printf("This doesn't represent the sides of a triangle");}
    }else{printf("This doesn't represent the sides of a triangle");}
  }else{printf("An entered value is negative or equal to zero. Please enter the numbers again.");}
  return 0;
}
