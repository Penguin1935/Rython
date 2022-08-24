from getpass import getpass
import time
import os

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
[1] Create An Account
[2] Login
""")

setup = input("[?]: ")


if setup == "1":
    name = input(str("Please Enter Name to be Displayed: "))
    pas = getpass(str("Please Enter Your Password to Login: "))
    with open('user/username.pass', 'w') as f:
        f.writelines(name)

    with open('user/password.pass', 'w') as f:
        f.writelines(pas)
    print("Setup Complete.")
    print("Opening Login... ")
    time.sleep(2)
    os.startfile('Login.py')

if setup == '2':
    login_pass = open('user/password.pass')
    login_name = open('user/username.pass')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = getpass(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        os.startfile("Login.py")
        break
    else:
        print("Wrong Password.")