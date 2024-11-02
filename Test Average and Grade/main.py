def inputs():
    user_scores = input("Enter five test scores separated by commas: ")
    return [int(number) for number in user_scores.split(",")]

def determine_grade(number):
    if 90 <= number <= 100:
        letter_grade = "A"
    elif 80 <= number <= 89:
        letter_grade = "B"
    elif 70 <= number <= 79:
        letter_grade = "C"
    elif 60 <= number <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

def show_the_letter_grade(number, letter_grade):
   print("{:.1f} is {}\n".format(number, letter_grade))

def calculate_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("The average test scores are: {:.1f} which is {}".format(average, grade))

list = inputs()
for n in list:
    show_the_letter_grade(n, determine_grade(n))
calculate_average(list)
