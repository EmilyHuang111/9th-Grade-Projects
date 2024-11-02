import os 
import pickle

# Create a dictionary or load an existing dictionary file
userInfo = {}
if os.path.exists("userInfo.pickle"):
  userInfo = pickle.load(open("userInfo.pickle","rb"))
  pass
else:
  passwords = open("userInfo.pickle","x")

# Create a menu
menu_option = ("1","2","3","4","5")
def menu():
  while(True):
    print("------------------ Menu ---------------- \n")
    print("1: Look up a person's password.\n")
    print("2: Add new username and password.\n")
    print("3: Change an existing password.\n")
    print("4: Delete an existing username and password.\n") 
    print("5: Save file and exit the program.\n")     
    print()
    userChoice = input("Please type 1, 2, 3, 4 and 5 to select one of the above options. ")
    if userChoice in menu_option:
      if userChoice == "1":
        userName = input("Please type in the person's username:")
        if(userName in userInfo):
          print("The person's password is " + userInfo[userName])
        else:
          print("The username dosen't exist. Use Option 2 to add username and password.\n")
      if userChoice == "2":
        userName = create_username()
        if userName in userInfo:
          print("The username already exists. Please use Option 2 to select a different username.\n")
        else:
          password = create_password()
          userInfo[userName] = password
          print("Your username and password have been added to the database.\n")
      if userChoice == "3": 
        print("Let's change an existing password.\n")
        userName = input("Please type in the person's username: ")
        if(userName in userInfo):
          password = create_password()
          userInfo[userName] = password    
          print("You have changed the person's password. \n")
        else:
          print("The username dosen't exist. Select Option 3 to type in the person's username again or select Option 2 to add username and password.\n")
      if userChoice == "4":
        print("Let's delete an existing username and password.\n") 
        userName = input("Please type in the person's username to delete:")
        if(userName in userInfo):
          del userInfo[userName]
          print("The username and password have been successfully deleted.\n")
        else:
          print("The username dosen't exist. Please verify the username and try again.\n")    
      if userChoice == "5":   
        break
    else:
          print("Your choice dosen't exist. Please type in correct choice. \n")
        
def create_username():
  while(True):
    user = input("Please enter a valid email as your username (including a @ and a . ): ")
    if("@" in user) and ("." in user):
      print("The username is valid.\n")
      return (user)
      break
    else:
      print("The username is invalid. Please try again.\n")

def create_password():
     while(True):
       password = input("Please enter a valid password with at least 8 characters, at least one uppercase letter, at least one lowercase letter, and at least one numeric digit: ")
       if len(password) < 8:
           print ("Make sure your password is at least 8 characters.")
           if not any(chr.isdigit() for chr in password):
             print("Make sure your password has a number.")
           if not any(chr.isupper() for chr in password):
             print("Make sure your password has an uppercase letter.")
           if not any(chr.islower() for chr in password):
             print("Make sure your password has a lowercase letter.")
       elif not any(chr.isdigit() for chr in password):
           print("Make sure your password has a number.")
           if not any(chr.isupper() for chr in password):
             print("Make sure your password has an uppercase letter.")
           if not any(chr.islower() for chr in password):
             print("Make sure your password has a lowercase letter.")
       elif not any(chr.isupper() for chr in password):
           print("Make sure your password has an uppercase letter.")
           if not any(chr.islower() for chr in password):
             print("Make sure your password has a lowercase letter.")       
       elif not any(chr.islower() for chr in password):
           print("Make sure your password has a lowercase letter.")
       else:
           print("Your password is valid.\n")
           return (password)
           break
menu();
# Save dictionary to a pickle file
with open("userInfo.pickle", "wb") as file:
  pickle.dump(userInfo,file,pickle.HIGHEST_PROTOCOL)
print("Your file has been successfully saved.")
