answer = input('Please enter a word or press enter to stop: ')
total = 0
count = 0

while answer != '':
  total+=len(answer)
  count += 1
  answer = input('Please enter a word or press enter to stop: ')

if count!=0:
  average = total/count
  average = round(average)
  
  print("The average length of word is: ", average)
              
