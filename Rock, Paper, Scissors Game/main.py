import random
c = random.randint(1, 3)
userInput = input("Enter either rock, paper, or scissors: ") 
label = "Computer's Choice: "
if c == 1:
  computer = "rock"
elif c == 2:
  computer = "paper"
else:
  computer = "scissors"
print(label + computer)  
def determine_winner(computer,userInput):
    if computer == "rock" and userInput == "scissors":
        detWinner = "Computer Won! The rock smashes the scissors."
    if computer == "scissors" and userInput == "rock":
        detWinner = "You Won! The rock smashes the scissors."
    if computer == "scissors" and userInput == "paper":
        detWinner = "Computer Won! Scissors cuts paper."
    if computer == "paper" and userInput == "scissors":
        detWinner = "You Won! Scissors cuts paper."
    if computer == "paper" and userInput == "rock":
        detWinner = "Computer Won! Paper wraps rock."     
    if computer == "rock" and userInput == "paper":
        detWinner = "You Won! Paper wraps rock."         
    return detWinner
if computer == userInput:
  print("It's a tie! Let's play again. Restart the program to play.")
else:
  winner = determine_winner(computer,userInput)
  print(winner)  




