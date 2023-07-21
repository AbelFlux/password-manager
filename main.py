import os
from rgbprint import gradient_print,Color
import win32gui, win32con
import time
from cryptography.fernet import Fernet

if not os.path.isfile("passwords.txt"):
   open("passwords.txt", "a").write("")

def generatepassword():
    print(f"{Fernet.generate_key()}")
    print("wip")

    input("Press enter to continue...")
    
def newpassword():
    f = open("passwords.txt", "a")
    usernewwebsite = input("What website is the password for? ")
    usernewusername = input("What username are you using? ")
    usernewpassword = input("What password are you using?")
    f.write(f'''Site: {usernewwebsite}|Username: {usernewusername}|Password: {usernewpassword}\n''')
    f.close()

def viewpassword():
    f = open("passwords.txt", "r")
    for x in f:
        print(x)
        time.sleep(0.1)
    input("press enter to continue...")

def delete_line(filename, line_number):

    with open(filename) as file:
        lines = file.readlines()

    
        if (line_number <= len(lines)):

            del lines[line_number - 1]

            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)
     
        else:
            print(f"Line {line_number} not in file")
            print("Files has", len(lines), "lines.")
            input("Press enter to continue...")


def title():
    os.system("title Password Manager")

def clear():
    os.system("cls")

def exit():
    os.system("exit")
    
def logo():
    clear()
    gradient_print("""


    
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ \



    """, start_color=Color(65, 105, 225),end_color=Color(255, 229, 180))
logo()
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
delete_filename = "passwords.txt"

def menu():
    while True:
        logo()
        title()
        gradient_print("""
        [1] Enter New Password
        [2] Remove Password
        [3] View Passwords  
        [4] Generate Password
        [0] Exit
        """,start_color=Color(65, 105, 225),end_color=Color(255, 229, 180))
        choice = int(input(">"))
        if choice == 1:
            newpassword()
        elif choice == 2:
            delete_line_number = int(input("What line is the password on? "))
            delete_line(delete_filename, delete_line_number)
        elif choice == 3:
            viewpassword()
        elif choice == 4:
            generatepassword()
        elif choice == 0:
            delete_line()


            
menu()       
