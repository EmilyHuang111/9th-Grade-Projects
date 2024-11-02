import os
import pickle
import consolemenu
from consolemenu import *
from consolemenu.items import *

studentInfo = {}
if os.path.exists("studentInfo.pickle"):
  studentInfo = pickle.load(open("studentInfo.pickle","rb"))
  pass
else:
  studentIDs = open("studentInfo.pickle","x")
def add_ID():
  print("Let's add a new ID and major \n")        
  while(True):
    student_ID = input("Please enter a new student ID (enter a six digit number only): ")
    if student_ID in studentInfo:
      print("This student already exists in the database. Make sure you specify the correct ID and try again.\n")
    elif len(student_ID) != 6:
      print ("Make sure the student ID has exact six digits.")
      if student_ID.isdigit() == False:
        print ("Make sure the student ID has only digits and no other character.\n")      
    elif student_ID.isdigit() == False:
      print ("Make sure the student ID has only digits and no other character.\n")
    else:
      print("Your student ID is valid.\n")
      major = input("Please enter the student's college major: ")
      studentInfo[student_ID] = major
      print("The student ID and college major have been successfully added to the database.\n")
      break
  x=(input("Hit enter to return to menu"))
def delete_ID():
  print("Let's delete a student ID and college major! \n")    
  while(True):
    student_ID = input("Please enter the student ID that you want to delete: ")
    if(student_ID in studentInfo):
      del studentInfo[student_ID]
      print("The student ID and college major have been successfully deleted.\n")
      break
    else:
      print("The student ID dosen't exist. Please verify the ID and try again.\n")
  x=(input("Hit enter to return to menu"))      
def change_major():
  print("Let's change the college major of a student!\n")  
  while(True):
    student_ID = input("Please enter a student ID that you want to change his/her college major: ")
    if(student_ID in studentInfo):
      print("The person's current college major is " + studentInfo[student_ID] + ".")      
      major = input("Please enter a new major for the student: ")
      studentInfo[student_ID] = major
      print("The student's college major has been successfully changed.\n")
      break
    else:
      print("The student ID dosen't exist. Please verify the ID and try again.\n")
  x=(input("Hit enter to return to menu"))  
def lookup_ID():
  print("Let's check if a student ID exits in the database! \n")      
  while(True):
    student_ID = input("Please enter a student ID (enter a six digit number only): ")
    if len(student_ID) != 6:
      print ("Make sure the student ID has exact six digits. \n")
    elif student_ID.isdigit() == False:
      print ("Make sure the student ID has only digits and no other character.\n")
    else:
      break
  if student_ID in studentInfo:
    print("This student exists in the database.")
    print("The person's college major is " + studentInfo[student_ID] + ". \n")
    x=(input("Hit enter to return to menu"))    
  else:
    print("This student dosen't exist in the database.\n")
    x=(input("Hit enter to return to menu"))  
    
def Printer():
  print(studentInfo)
  x = input("Hit enter to return to menu")
  
menu = ConsoleMenu("Console menu Practice", "Student IDs and College Majors")
function_item1 = FunctionItem("To add a new ID and major.", add_ID)
function_item2 = FunctionItem("To delete an existing ID and major.", delete_ID)
function_item3 = FunctionItem("To change an existing major for an ID.", change_major)
function_item4 = FunctionItem("To look up an existing ID and major.", lookup_ID)
function_item5 = FunctionItem("Print Database", Printer)
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)
menu.append_item(function_item5)

menu.show()
# Save dictionary to a pickle file
with open("studentInfo.pickle", "wb") as file:
  pickle.dump(studentInfo,file,pickle.HIGHEST_PROTOCOL)
print("Your file has been successfully saved.")
