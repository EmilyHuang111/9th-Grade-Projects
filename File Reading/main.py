import os
import time

if os.path.exists("demofile.txt"):
  f=open("demofile.txt","rt")
else:
  f=open("demofile.txt","x")
f.close()

f=open("demofile.txt","w")
f.write("Hello from demofile.txt\nThis file is for testing purposes\nGood Luck!")
f.close()

f=open("demofile.txt","r")
print(f.read())
f.close()
f=open("demofile.txt","r")
print(f.read(10))
f.close()
f=open("demofile.txt","r")
print(f.readline())
f.close()

f=open("demofile.txt","a")
f.write("\n Here is some new content")
f.close()

f=open("demofile.txt","r")
for line in f:
  print (line)
f.close()

time.sleep(10)
os.remove("demofile.txt")


