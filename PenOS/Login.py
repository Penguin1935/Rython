from getpass import getpass
import os
import time

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
print("""
[Login] To Login
""")

Login_A = input()

if Login_A == 'Login':
    login_pass = open('user/password.pass')
    login_name = open('user/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = getpass(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        print("Getting Password...")
        time.sleep(0.2)
        print("Getting User...")
        time.sleep(0.2)
        print("Downloading PenOS Packages...")
        time.sleep(0.2)
        print("Extracting PenOS Packages...")
        time.sleep(0.2)
        print("Opening PenOS Packages...")
        time.sleep(0.2)
        print("Finished...")
        time.sleep(0.2)
        print("Opening PenOS... ")
        time.sleep(1)
        os.startfile("Desktop.py")
        break
    else:
        print("Wrong Password.")
