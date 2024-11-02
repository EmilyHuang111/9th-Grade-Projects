import random
def menu():
  print("1. ADD\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
  choice = int(input("Enter choice: "))
  return choice

def sum(num1,num2):
  return num1+num2

def divide(num1,num2):
  if num2 == 0:
    return 'undefined'
  else:
    return num1/num2
  
def start():
  menuChoice = menu()
  num1=random.randint(0,10)
  num2=(random.randint(0,10))
  if menuChoice ==1:
    print(f"The sum of {num1} and {num2} is {sum(num1,num2)}")
    start()

  elif menuChoice ==4:
    
    print(f"The quotient of {num1} and {num2} is {divide(num1,num2)}")
    start()

  elif menuChoice ==5:
    exit()

  else: 
   print("That choice does not exist ")
  start()


start()
