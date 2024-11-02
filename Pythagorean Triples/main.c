//Program to determine all the Pythagorean Triples
#include <stdio.h>
int main(void) {
  int count = 0;
  for (unsigned int i = 1; i <= 500; ++i){
  for(unsigned int j = i; j <= 500; ++j){
    for (unsigned int k = j; k <= 500; ++k){
      if(i*i + j*j == k*k){
         printf("%d %d %d\n", i,j,k);
        count++;
      }
    }
  }
}
  printf("%d",count);
  return 0;
}
