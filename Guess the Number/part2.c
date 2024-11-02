//Guess the number program with modifications
#include <stdio.h>
#include<stdlib.h>
#include <time.h>

int main(void) {
 int num,guess = 0, count = 0;
 char replay;
  srand(time(NULL));
  num = rand()%1000 + 1; 
  //printf("%d\n", num);
  printf("%s","I have a number between 1 and 1000.\nCan you guess my number?\nPlease type your first guess.\n");
  scanf("%d", &guess);
  count++;
  
  while(guess != -1){
    if(guess == num){ 
      printf("%s","Excellent! You guessed the number!\n");
      if(count < 10){
        printf("%s", "Either you know the secret or you got lucky!\n");
      }
      if(count == 10){
        printf("%s", "Ahah! You know the secret!\n");
      }
      if(count > 10){
        printf("%s", "You should be able to do better! Why should it take no more than 10 guesses?\n");
      }
      printf("%s","Would you like to play again (y or n)?");
      scanf(" %c", &replay);
      if(replay == 'n'){
        break;
      }else{
        num = rand()%1000 + 1; 
        //printf("%d\n", num);
        printf("%s","I have a number between 1 and 1000.\nCan you guess my number?\nPlease type your first guess.\n");
        scanf("%d", &guess);
        count = 0;
        count++;
      }
    }
    if(guess > num){
         printf("%s","Too high. Try again.\n");
         scanf("%d", &guess);
         count++;
    }
    if(guess < num){ 
         printf("%s","Too low. Try again.\n");
         scanf("%d", &guess);
         count++;
    }
  }
  return 0;
}
