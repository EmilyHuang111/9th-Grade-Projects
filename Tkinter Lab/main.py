import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os 
import pickle
studentInfo = {}
info_list = {'firstName':'','lastName':'','grade':'','teacher':'','classes':''}
if os.path.exists("studentInfo.pickle"):
  studentInfo = pickle.load(open("studentInfo.pickle","rb"))
  pass
else:
  passwords = open("studentInfo.pickle","x")
root = tk.Tk()
root.geometry("600x600")
root.title("Computer Science Info Form")

#Define variables
student_id = tk.IntVar() #entry box variable 1
first_name = tk.StringVar() #entry box variable 2
last_name = tk.StringVar() #entry box variable 3
student_grade = tk.IntVar() #radio button variable
student_teacher = tk.StringVar() #combox variable
student_class1 = tk.IntVar() #checkbox varible 1
student_class2 = tk.IntVar() #checkbox varible 2
student_class3 = tk.IntVar() #checkbox variable 3
student_class4 = tk.IntVar() #checkbox variable 4
student_class5 = tk.IntVar() #checkbox variable 5
student_class6 = tk.IntVar() #checkbox variable 6
student_class7= tk.IntVar() #checkbox variable 7
student_class8 = tk.IntVar() #checkbox variable 8
student_class1.set = 0
student_class2.set = 0
student_class3.set = 0
student_class4.set = 0
student_class5.set = 0
student_class6.set = 0
student_class7.set = 0
student_class8.set = 0
search_id = tk.IntVar() #entry box variable 4

#Create student ID entry
ID_label = tk.Label(root, text = "Please enter your student ID.")
ID_label.grid(row = 0, column = 0)
ID_entry = tk.Entry(root, textvariable = student_id)
ID_entry.grid(row = 0, column = 1)

#Create first and last name entries
first_name_label = tk.Label(root, text = "Please enter your first name.")
first_name_label.grid(row = 1, column = 0)
first_name_entry = tk.Entry(root, textvariable = first_name)
first_name_entry.grid(row = 1, column = 1)
last_name_label = tk.Label(root, text = "Please enter your last name.")
last_name_label.grid(row = 2, column = 0)
last_name_entry = tk.Entry(root, textvariable = last_name)
last_name_entry.grid(row = 2, column = 1)

#Create grade radio buttons
grade_label = tk.Label(root, text = "Please select the grade you are in.")
grade_label.grid(row = 3, column = 0)
radiobutton1 = tk.Radiobutton(root, text = "9th grade", variable = student_grade, value = 9)
radiobutton1.grid(row = 3, column = 1)
radiobutton2 = tk.Radiobutton(root, text = "10th grade", variable = student_grade, value = 10)
radiobutton2.grid(row = 4, column = 1)
radiobutton3 = tk.Radiobutton(root, text = "11th grade", variable = student_grade, value = 11)
radiobutton3.grid(row = 5, column = 1)
radiobutton4 = tk.Radiobutton(root, text = "12th grade", variable = student_grade, value = 12)
radiobutton4.grid(row = 6, column = 1)

#Create teacher selection combo button
teachers = ("Mrs. Demosthenes", "Mr. Stern", "Mr. Rivero", "Mrs. Behar")
teacher_label = tk.Label(root, text = "Computer Science teacher:")
teacher_label.grid(row = 7, column = 0)
teacher_combo  = ttk.Combobox(root, textvariable = student_teacher)
teacher_combo['values'] = teachers
teacher_combo['state'] = 'readonly'
teacher_combo.grid(row = 7, column = 1)

#Create class select check boxes
class_label = tk.Label(root, text = "Computer Science classes that you have taken:")
class_label.grid(row = 8, column = 0)
cb1 = tk.Checkbutton(root, text = "AP CSA                                     ", variable = student_class1)
cb1.grid(row = 9, column = 1)
cb2 = tk.Checkbutton(root, text = "AP CSP                                     ", variable = student_class2)
cb2.grid(row = 10, column = 1)
cb3 = tk.Checkbutton(root, text = "CSE                                          ", variable = student_class3)
cb3.grid(row = 11, column = 1)
cb4 = tk.Checkbutton(root, text = "PWP                                         ", variable = student_class4)
cb4.grid(row = 12, column = 1)
cb5 = tk.Checkbutton(root, text = "Machine Learning & AI (S1)      ", variable = student_class5)
cb5.grid(row = 13, column = 1)
cb6 = tk.Checkbutton(root, text = "Cybersecurity and Defence (S2)", variable = student_class6)
cb6.grid(row = 14, column = 1)
cb7 = tk.Checkbutton(root, text = "Big Data                                   ", variable = student_class7)
cb7.grid(row = 15, column = 1)
cb8 = tk.Checkbutton(root, text = "Web/App Development (S1)     ", variable = student_class8)
cb8.grid(row = 16, column = 1)

#Funtion to show messagebox and save input information
def submit():
  studentID=ID_entry.get()
  firstName=first_name_entry.get()
  lastName=last_name_entry.get()
  studentGrade=student_grade.get()
  studentGrade=str(studentGrade)
  studentTeacher=student_teacher.get()
  studentClasses=[]
  classes= ""
  if student_class1.get()==1:
    classes+="AP CSA\n"
    studentClasses.append("AP CSA")
  if student_class2.get()==1:
    classes+="AP CSP\n"
    studentClasses.append("AP CSP")
  if student_class3.get()==1:
    classes+="CSE\n"
    studentClasses.append("CSE")
  if student_class4.get()==1:
    classes+="PWP\n"
    studentClasses.append("PWP")
  if student_class5.get()==1:
    classes+="Cybersecurity and Defenses\n"
    studentClasses.append("Cybersecurity and Defenses")
  if student_class6.get()==1:
    classes+="Web/App Development\n"
    studentClasses.append("Web/App Development")
  if student_class7.get()==1:
    classes+="Big Data\n"
    studentClasses.append("Big Data")
  if student_class8.get()==1:
    classes+="Machine Learning & AI\n"
    studentClasses.append("Machine Learning & AI")
  student_info=info_list.copy()
  student_info['firstName']=firstName
  student_info['lastName']=lastName
  student_info['grade']=studentGrade
  student_info['teacher']=studentTeacher
  student_info['classes']=classes
  studentInfo[studentID]=student_info
  message="The form has been submitted. \nYour ID is "+studentID+".\nYour first name is "+firstName+".\nYour last name is "+lastName+".\nYour grade is "+studentGrade+".\nYour teacher is "+studentTeacher+".\nYou have taken these classes:\n"+classes+""
  messagebox.showinfo('Confirmation',message)
  # Save dictionary to a pickle file
  student_file = open("studentInfo.pickle", "wb")
  with student_file as file:
    pickle.dump(studentInfo,file,pickle.HIGHEST_PROTOCOL)
  student_file.close()

#Function to check if student ID exists 
def ID_exists(id):
  check = False
  keys = studentInfo.keys()
  keys = list(keys)
  if keys == ():
    return False
  else:
    for ids in keys:
      if ids == id:
        check = True
    return check

#Function to search student information based on ID                  
def search(id):
  ids = id.get()
  ids = str(ids)
  if ID_exists(ids):
    first_name = studentInfo[ids]['firstName']
    last_name = studentInfo[ids]['lastName']  
    grade = studentInfo[ids]['grade']
    teacher = studentInfo[ids]['teacher']
    class_list = studentInfo[ids]['classes']
    message="Your ID is "+ids+".\nYour first name is "+first_name+".\nYour last name is "+last_name+".\nYour grade is "+grade+".\nYour teacher is "+teacher+".\nYou are taking these classes: "+class_list+"."
    messagebox.showinfo('',message)
  else:
    messagebox.showinfo('Error','ID does not exist please try again')

#Function to close the interface
def exit():
  messagebox.showinfo('Selection', "Exiting Program...")
  root.destroy()

#Create save button to add informtion to the database
saveButton = tk.Button(root, text = "Submit",command=submit)
saveButton.grid(row = 17, column = 0)

#Create student ID to search entry and button
search_ID_label = tk.Label(root, text = "Enter student ID to search.")
search_ID_label.grid(row = 18, column = 0)
search_ID_entry = tk.Entry(root, textvariable = search_id)
search_ID_entry.grid(row = 18, column = 1)
searchButton=tk.Button(root,text="Search",command=lambda:search(search_ID_entry))
searchButton.grid(row = 19, column = 0)

#Create quick button to close the interface
exitButton = tk.Button(root, text = "Exit", command = exit)
exitButton.grid(row = 20, column = 0)

root.mainloop()
