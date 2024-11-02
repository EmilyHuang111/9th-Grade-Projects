user_numbers = []

print("Enter 20 numbers: ")
for i in range(1, 21):
  number = float(input(f"Input number {i}: "))
  user_numbers.append(number)

num_lowest = 9999999999999999999
num_highest = 0
sum = 0

for i in range(len(user_numbers)):
  if user_numbers[i] <  num_lowest:
    num_lowest = user_numbers[i]
  if user_numbers[i] >  num_highest:
    num_highest = user_numbers[i]
  sum += user_numbers[i]
avg = sum/20

print(f"The lowest number in the list: {num_lowest}")
print(f"The highest number in the list: {num_highest}")
print(f"The total of the numbers in the list: {sum}")
print(f"The average of the numbers in the list: {avg}")
