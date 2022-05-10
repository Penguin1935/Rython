from bdb import Breakpoint
from cgitb import reset
import time
import os
import socket
import psutil

battery = psutil.sensors_battery()
login_pass = open('user/password.pass')
login_name = open('user/username.pass')
l_p = login_pass.read()
l_n = login_name.read()
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
print("Welcome to PenOS, " + l_n)
print("The Date Is: " + time.strftime("%d/%m/%y"))
print("The Battery Percent is")
print(battery.percent)
print("""
[1] To Open Google
[2] To Open TextEditor
[3] To Open File Exploer
[4] To Configure BiOS
[5] To Close OS Safely
[6] To Go Back To Login
[7] Play Snake
""")

select = input("[?]: ")

if select == "1":
    os.startfile('brows.py')

if select == "2":
   os.startfile('edit.py')

if select == "3":
   os.startfile('file.py')

if select == "5":
   input("Press Enter To Close: ")

if select == "6":
   os.startfile("PenOS.py")

if select == "7":
   os.startfile("Python.py")

if select == "4":
 while True:
   b_login = input(str("Please Enter The Password To " + l_n + " To Open BiOS: "))
   if b_login == l_p:
      print("Opening BiOS")
      print("""
      [1] To Change Username
      [2] To Change Password
      [3] To Reset All Data
      """)
      host_name = socket.gethostname()
      host_ip = socket.gethostbyname(host_name)
      print("[1] USER NAME: " + l_n)
      print("[2] USER PASSWORD: " + l_p)
      print("HOST NAME: " + host_name)
      print("LOCAL IPS: " + host_ip)
      edit_b = input("Enter [1] or [2] to change setting: ")

      if edit_b == "1":
         edit_n = input("Enter New Username: ")
         with open('user/username.txt', 'w') as f:
            f.writelines(edit_n)
         print("Username Changed To: " + edit_n)
         input("Press Enter To Close Window: ")

         if edit_b == "2":
            edit_p = input("Enter New Password: ")
            with open('user/password.txt', 'w') as f:
               f.writelines(edit_p)

               print("Password Changed To: " + edit_p)
               input("Press Enter To Close")

      else:
          print("Wrong Password To " + l_n)
