#include <stdio.h>
int main(void) {
  int x=1;
  int y=2;
  int a=3;
  int b=4;
  int g=5;
  int i=6;
  int j=7;

  printf("The current values are: \n");
  printf("x = %d, y = %d \n", x,y);
  printf("a = %d, b = %d, g = %d\n", a, b, g);
  printf("i = %d, j = %d \n", i, j);
  if ((!(x < 5 && ! (y >= 7))) == (!(x < 5 || y >= 7))){
    printf("!(x < 5) && !(y >= 7) is equivalent to !(x < 5 || y >= 7)\n");
  }else{
    printf("!(x < 5 && !(y >= 7) is not equivalent to !(x < 5 || y >= 7)\n");
  }
    if((!(a == b) || !(g != 5)) == (!(a == b && g != 5))){
      printf("!(a == b) || !(g != 5) is equivalent to !(a == b && g != 5)\n");
    }else{
      printf("!(a == b) || !(g != 5) is not equivalent to !(a == b && g != 5)\n");
    }
  if (!((x <= 8) && (y > 4)) == (!(x <= 8) || !(y > 4))){
    printf("!((x <= 8) && (y > 4)) is equivalent to !(x <= 8) || !(y > 4)\n");
    }else{
    printf("!((x <= 8) && (y > 4)) is not equivalent to !(x <= 8) || !(y > 4)\n");
    }
  if (!((i > 4) || (j <= 6)) == (!(i > 4) && !(j <= 6))){
    printf("!((i > 4) || (j <= 6)) is equivalent to !(i > 4) && !(j <= 6)");
    }else{
    printf("!((i > 4) || (j <= 6)) is not equivalent to !(i > 4) && !(j <= 6)");
    }
  return 0;
}
