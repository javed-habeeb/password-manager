import random
import string
import json
import os
import base64
from pprint import pprint
from cryptography.fernet import Fernet
from key_manager import load_key #the function to be imported
import traceback

passwords={}
password=""
ENCRYPTION_KEY = load_key()
cipher = Fernet(ENCRYPTION_KEY)

def show_password_memory():
    while True:
        print("specific password or the complete dict\n1)spcific(a)\n2)complete(b)\ntype 'esc' to exit\n")
        request=input("").lower()
        
        #logic goes here
        if request == "a":
            key = input("enter the key: ")
            print("\n")
            if key in passwords:
                decrypted_password = cipher.decrypt(passwords[key]).decode()
                print(f"password for {key}: {decrypted_password}")
            else:
                print(f"key {key} doesnt exist in memory")
        elif request == "b":
            if passwords:
                for key, encrypted_pass in passwords.items():
                    decrypted_password = cipher.decrypt(encrypted_pass).decode()
                    print(f"{key}: {decrypted_password}")
            else:
                print("no password stored")

        elif request == "esc":
            break
        else:
            print("incorrect input")
        #logic ends here

    #print('function 'show_password_memory')
def generate_password(choice):
    global password
    if choice == 1:
        password="".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    elif choice == 2:
        password="".join(random.choice(string.digits) for _ in range(8))
    elif choice == 3:
        password="".join(random.choice(string.ascii_letters) for _ in range(8))
    elif choice == 4:
        print("exiting")
        return
    else:
        print("invalid input,try again")
        return
    print(f"generated password: {password}")

def save_password():
    global password
    if not password:
        print("no password generated to save")
        return
    while True:
        print(r"save password? (Y\N)")
        choice = input("").upper()
        if choice == "Y":
            name=input("what key would this password be named as?\n")
            if name not in passwords:
                encrypted_password = cipher.encrypt(password.encode())
                passwords[name]=encrypted_password
                print(f"key-password pair  saved as {name}.")
                break
            else:
                print("key already exists for another password")
        elif choice == "N":
            print("password not saved,exiting...")
            break
        else:
            print("wrong input.type Y or N")

def save_to_file(filename):
    if not passwords:
        print("no password saved,action can't be done")
        return
    try:
        with open(f"{filename}.json","w") as file:
            json.dump({k: v.decode() for k, v in passwords.items()}, file)
            print(f"password(s) saved to {filename}.json")
    except Exception as e:
        print(f"error saving to file: {e}")

def read_from_file(filename):
    file_path=f"{filename}.json"
    #check if the file is empty or improperly structured
    if os.path.exists(file_path) and os.stat(file_path).st_size > 0: #if the path exists and size greater than 0B
        #error handling to check if its a valid json file
        try:
            with open(file_path,"r") as file:
                data = json.load(file) #attempts to load the file
                section_header("Decrypted Passwords from File-start")
                for key, encrypted_pass in data.items():
                    decrypted = cipher.decrypt(encrypted_pass.encode()).decode()
                    passwords[key] = cipher.encrypt(decrypted.encode())
                    print(f"{key}: {decrypted}")
                section_header("Decrypted Passwords from File-end")
        except json.JSONDecodeError: #if its not a structured json
            print("file not structured properly as a JSON file")
        except Exception as e:
            print(f"error reading from file: {e}")
            traceback.print_exc()
    else:
        print("error: file is empty or Does Not Exist")

def section_header(title):
    print("\n" + "="*50)
    print(f"{title.center(50)}")
    print("="*50 + "\n")


#main program loop
def main():
    while True:
        section_header("PASSWORD GENERATOR")
        print("\nwhat would you wish to do\ncreate a password --1\nstore a password --2\nshow the dictionary storing the password --3\nexit --4\nsave to file --5\ndisplay file --6\n")
        user_choice = input().strip()
        if user_choice == "1":
            section_header("generate a password")
            print("\nwhat kind of password do you want\n1) mixed\n2) num\n3) letter\n4) exit\n")
            try:
                choice = int(input())
                generate_password(choice)
            except ValueError:
                print("invalid input.please enter a number")
        elif user_choice == "2":
            section_header("saving the password")
            print(f"recently created password was: {password}")
            save_password()
        elif user_choice == "3":
            section_header("show from password memory")
            show_password_memory()
        elif user_choice == "5": #save to file
            section_header("save to file")
            filename=input("which file do you want it to be saved(without the extension): ")
            save_to_file(filename)
        elif user_choice == "6":
            section_header("display from file")
            filename=input("the file you want to read data from: ")
            read_from_file(filename)
        elif user_choice == "4":
            print("exiting the program\n")
            break
        else:
            print("invalid choice.please select a valid option")
if __name__ == "__main__":
    main()    
