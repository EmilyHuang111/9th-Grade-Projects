import os 
if os.path.exists("demofile.txt"):
  pass
else:
 passwords = open("demofile.txt", "x")

def create_username():
  while(True):
    user = input("Please enter a valid email as your username (including a @ and a . ): ")
    if("@" in user) and ("." in user):
      print("The username is valid")
      return (user)
      break
    else:
      print("The username is invalid. Please try again.")

def create_password():
     while(True):
       password = input("Please enter a valid password with at least 8 characters, at least one uppercase letter, at least one lowercase letter, and at least one numeric digit: ")
       if not password_exists(password):
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
           print("Your password is valid")
           return (password)
           break
       else:
          print("Your password already exists in the file.")
         

def save_password(password):
  passwords = open("demofile.txt", "a")
  passwords.write(password)
  passwords.write("\n")
  passwords.close()

def password_exists(x):
  y = False
  passwords = open("demofile.txt", "r")
  for i in passwords:
      if x == i.strip():
        y = True
        break
  return y
  passwords.close()
    
user = create_username()
password = create_password()
print("Your username is " + user)
print("Your password is " + password)
save_password(password)
