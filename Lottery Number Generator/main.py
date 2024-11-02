import random
user_numbers = []
random_numbers = []
for number in range(1, 8):
 number = random.randint(0, 9)
 random_numbers.append(number)
print("The program generated the following numbers: ")
print(random_numbers)
print("Choose 7 integer numbers between 0 and 9: ")
for i in range(1, 8):
  number = int(input(f"Input number {i}: "))
  user_numbers.append(number)

numMatch = 0
for i in range(len(user_numbers)):
  if user_numbers[i] ==  random_numbers[i]:
    print(f"Input number {i+1} matches the program: {user_numbers[i]}")
    numMatch += 1
if numMatch == 7:
  print("Congratulations! You won the lottery!!!")
else:
  print("Unfortunately, you didn't win the lottery.")

