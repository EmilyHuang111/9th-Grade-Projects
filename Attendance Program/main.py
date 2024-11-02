import os 
import pickle
studentInfo = {}
attendance_list = {'M':'','T':'','W':'','R':'','F':''}
if os.path.exists("studentInfo.pickle"):
  studentInfo = pickle.load(open("studentInfo.pickle","rb"))
  pass
else:
  passwords = open("studentInfo.pickle","x")
menu_option = ("1","2","3","4","5")
def menu():
  while(True):
    print("------------------ Menu ---------------- \n")
    print("1: To add a student.\n")
    print("2: To remove a student.\n")
    print("3: To take attendance.\n")
    print("4: To show attendance.\n") 
    print("5: Save file and exit the program.\n")     
    
    print()
    userChoice = input("Please type 1, 2, 3, 4 or 5 to select one of the above options. ")
    if userChoice in menu_option:
      if userChoice == "1":
        print("Let's add a student to the class! \n")         
        add_student()
      if userChoice == "2":
        print("Let's remove a student from the class! \n")      
        remove_student()
        
      if userChoice == "3": 
        print("Let's take attendance for the class!\n")
        take_attendance()
      if userChoice == "4":
        show_attendance()
      if userChoice == "5": 
        exit_program()
        print("Your file has been successfully saved.")
        break
    else:
      print("Your choice dosen't exist. Please type in correct choice. \n")
def add_student():
  while(True):
    student = input("Please enter the name of the student to add: ")
    student = student.upper()
    if student in studentInfo:
      print("This student alread exists in the database. Make sure you specify the correct student name and try again.\n")
    else:
      studentInfo[student] = attendance_list.copy()
      print("Your student has been successfully added to the attendance sheet.\n")
      break
def remove_student():
  while(True):
    student = input("Please enter the exact name of the student to remove: ")
    student = student.upper()
    if(student in studentInfo):
      del studentInfo[student]
      print("The student has been successfully deleted.\n")
      break
    else:
      print("The student dosen't exist. Please verify the name of the student and try again.\n") 
def take_attendance():
    if studentInfo == {}:
      print("There is no student in the database.")
    else:
      while(True):
        day = input("Which day for the attendance? (Enter M, T, W, R, or F) \n")
        day = day.upper()
        if(day != 'M' and day != 'T' and day != 'W' and day != 'R' and day != 'F'):
          print("Please enter the correct day and try again.")
        else:
          for student in studentInfo.keys():
            while(True):
              attendance = input("Please input if " + student + " is either present (P), absent (A), or tardy (T): ")
              attendance = attendance.upper()
              if(attendance != 'P' and attendance != 'A' and attendance != 'T'):
                print("Please enter the correct attendance and try again.")
              else:
                studentInfo[student][day] = attendance
                break
          break
def show_attendance():
  if studentInfo == {}:
    print("There is no student in the database.")
  else:
    print("Name\t\t\tM\tT\tW\tR\tF")
    for student in studentInfo.keys():
      mon = studentInfo[student]['M']
      tue = studentInfo[student]['T']
      wed = studentInfo[student]['W']
      thu = studentInfo[student]['R']
      fri = studentInfo[student]['F']
      print(student+"\t\t\t" + mon + "\t" + tue + "\t" + wed + "\t" + thu + "\t" + fri)
    print("(P = present, A = absent, T = tardy)")
def exit_program():
  # Save dictionary to a pickle file
  student_file = open("studentInfo.pickle", "wb")
  with student_file as file:
    pickle.dump(studentInfo,file,pickle.HIGHEST_PROTOCOL)
  student_file.close()
menu();
        
