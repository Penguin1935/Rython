import time
import os

print("""
      (^-^)
     <(###)>
        w

        
██████╗░███████╗███╗░░██╗░░░░█████╗░░██████╗
██╔══██╗██╔════╝████╗░██║░░░██╔══██╗██╔════╝
██████╔╝█████╗░░██╔██╗██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══╝░░██║╚████║██╗██║░░██║░╚═══██╗
██║░░░░░███████╗██║░╚███║╚█║╚█████╔╝██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚══╝░╚╝░╚════╝░╚═════╝░
   """)

print("""
[1] Continue with setup
[2] Ive Already done setup
[Shut Down] To Shutdown
""")

setup = input("[?]: ")

if setup == "Shut Down":
    input("Are You Sure You Want To ShutDown?")

if setup == "1":
    name = input(str("Please Enter Name to be Displayed: "))
    pas = input(str("Please Enter Your Password to Login: "))

    with open('user/username.txt', 'w') as f:
        f.writelines(name)

    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("Setup Complete.")
    input("Press Enter To Close Window: ")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        os.startfile("home.py")
        break
    else:
        print("Wrong Password.")