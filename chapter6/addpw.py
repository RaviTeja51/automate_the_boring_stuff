 
#program to store passwords
import bcrypt
from pyperclip import copy
from getpass import getpass
import json
from sys import argv,exit


def get():
# gets the password
   name = input("Enter the account name:")
   temp = getpass("Enter the secret password to decrypt the password: ")
   
   with open("manager.json","r") as f:
     data = json.load(f) #gets the json object.
     
     if name not in data.keys():
       exit("Account doesn't exist")
     
     password = data[f"{name}"]
     copy(cipher(password,temp))
     exit("Successfully copied to  the clipboard")
      
 
    
def add():
# adds new password and account
    name = input("Enter the new  account name:")
    temp = getpass(f"Password for {name}: ")
    secret = getpass("Enter the secret password to encrypt the password: ")       
    new = {}
    new[name] = cipher(temp,secret) 
    count = input("Is this the first account which you are adding, Y/N: ")
    if count.upper() == "Y":
        with open("manager.json","w") as f:
          json.dump(new,f)
          exit("New account and password are added successfully")
    elif count.upper() == "N":  
        with open("manager.json","r") as f:
          data = json.load(f)
          data.update(new)
        with open("manager.json","w") as f:
         json.dump(data,f)
         exit("New Account and Password are added successfully") 
    else:
        exit("Enter either Y or N")

 
def update():#to change the password.
   name = input("Enter the  account name: ")
   pw = getpass(f"Old Password for {name}: ")
   temp = getpass("Enter the secret password to encrypt:")
   with open("manager.json","r") as f:
    data = json.load(f)
   print(cipher(data[f"{name}"],temp))
   if pw == cipher(data[f"{name}"],temp):
      password = getpass(f" New Password for {name}: ")
      if password == getpass(f"Enter the new password again"):
         data[f"{name}"] = cipher(password,temp)
         with open("manager.json","w") as f:
            json.dump(data,f)
            exit("You successfully added the new password")
         
      else:
         exit("Your passwords did not match")
   else:
      exit("Wrong Password")
    


def cipher(password,key): # to encrypt the password.
    ciphered = ""
    l = len(key)
    for i in range(len(password)):
        ciphered += chr(ord(password[i]) ^ ord(key[ i % l]))
    return ciphered
             
  
if __name__ == "__main__":
   if len(argv) != 2:
       exit("Usage: python3 password.py action where action is get,new,update")
   action = argv[1]
   pa = getpass("Enter the password to open the file: ")
   pa = pa.encode("utf-8")
   password = "UzumakiNaruto"
   hashed = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
   if bcrypt.checkpw(pa,hashed):
      if action =="get":
         get()
      elif action =="add":
         add()
      elif action =="update":
         update()
      else:
        exit("Invalid choice you can add, get, update password")
   else:

     exit("Invalid password")
   
   
