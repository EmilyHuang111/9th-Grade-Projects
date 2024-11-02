//Program to guess the number
#include <stdio.h>
#include<stdlib.h>
#include <time.h>

int main(void) {
 int num,guess = 0;
 char replay;
  srand(time(NULL));
  num = rand()%1000 + 1; 
  //printf("%d\n", num);
  printf("%s","I have a number between 1 and 1000.\nCan you guess my number?\nPlease type your first guess.\n");
  scanf("%d", &guess);
  
  while(guess != -1){
    if(guess == num){ 
      printf("%s","Excellent! You guessed the number!\nWould you like to play again (y or n)?");
      scanf(" %c", &replay);
      if(replay == 'n'){
        break;
      }else{
        printf("%s","I have a number between 1 and 1000.\nCan you guess my number?\nPlease type your first guess.\n");
        scanf("%d", &guess);
      }
    }
    if(guess > num){
         printf("%s","Too high. Try again.\n");
         scanf("%d", &guess);
    }
    if(guess < num){
         printf("%s","Too low. Try again.\n");
         scanf("%d", &guess);
    }
  }
  return 0;
}
