#imports
from getpass import getpass
import os
import time
import string
import random

length = 10

randomstr = ''.join(random.sample(string.ascii_letters+string.digits,length))

print("""


      (^-^)
     <(###)>
        W
  ____             ___  ____  
 |  _ \ ___ _ __  / _ \/ ___| 
 | |_) / _ \ '_ \| | | \___ \ 
 |  __/  __/ | | | |_| |___) |
 |_|   \___|_| |_|\___/|____/ 
                               
                      
""")
print("You need a Product Key")
print("Your Product Key Is: " + randomstr)

while True:
    login_name = open("user/username.pass")
    login_pass = open("user/password.pass")
    l_n = login_name.read()
    l_p = login_pass.read()
    Key = input("Please Enter A Product Key: ")

    if Key == randomstr:
      login = getpass(str("Please Enter The Password To " + l_n + ":"))
    else:
      print("Wrong Key")
      break
    if login == l_p:
        print("Getting Password...")
        time.sleep(0.1)
        print("Getting User...")
        time.sleep(0.4)
        print("Downloading PenOS Packages...")
        time.sleep(0.3)
        print("Extracting PenOS Packages...")
        time.sleep(0.3)
        print("Opening PenOS Packages...")
        time.sleep(0.6)
        print("Finished...")
        time.sleep(0.3)
        print("Opening PenOS... ")
        time.sleep(2)
        os.startfile("HomeStartScreen.py")
        break
    else:
        print("Wrong Password.")


    if Key == "1-11-11-11-12":
     login = getpass(str("Please Enter The Password To " + l_n + ": "))
    else:
      print("Wrong Key")
    if login == l_p:
        print("Getting Password...")
        time.sleep(0.1)
        print("Getting User...")
        time.sleep(0.4)
        print("Downloading PenOS Packages...")
        time.sleep(0.3)
        print("Extracting PenOS Packages...")
        time.sleep(0.3)
        print("Opening PenOS Packages...")
        time.sleep(0.6)
        print("Finished...")
        time.sleep(0.3)
        print("Opening PenOS... ")
        time.sleep(2)
        os.startfile("HomeStartScreen.py")
        break
    else:
        print("Wrong Password.")
