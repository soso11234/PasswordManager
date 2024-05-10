from Password import Password
from Map import Map
from Cipher import Cipher
from Id import Id
import os
class Manager():
    def __init__(self):
        self.map = Map()
        self.password = Password()
        self.id_instance = Id()
    
    def create_account(self):
        create_account = input("Write your account to sing up : ")
        if self.id_instance.create_id(create_account):
            return create_account
        else:
            return False
    
    def create_password(self,username):
        if self.password.create_password(username):
            return True
        else:
            return False
    
    def login(self,username):
        if self.password.match_password(username):
            return True
        else:
            return False
    
    def writing(self,username):
        making_category = input("What program/website do you want to write : ")
        making_id = input("Write account of the program/website : ")
        making_password = input("Write password of the account : ")
        cipher = Cipher(username)
        encrypted_password = cipher.encrypt(making_password)

        try:
            with open(f'{username}','a', encoding = 'utf-8') as f:
                f.write(making_category+'\n')
                f.write(making_id+'\n')
                f.write(encrypted_password+'\n')
        except Exception as e:
            print(f"Error : {e}")
            
    def reading(self,username):
        find_category = input("What program/website do you want to find : ")
        try:
            with open(f'{username}','r',encoding = 'utf-8') as f:
                lines = f.readlines()
                for i in range(0,len(lines)):
                    category = lines[i].strip()
                    if category == find_category:
                        print("Account found : ")
                        print("Program/website : ",category)
                        print("ID : ", lines[i+1].strip())
                        cipher = Cipher(username)
                        decrypted_password = cipher.decrypt(lines[i+2].strip())
                        print("Password : ", decrypted_password)
                        break
                    else:
                        print("Can't found ")
        except Exception as e:
            print(f"Error : {e}")

    def running(self):
        flag = True
        while flag:
            print("1. create account & password")
            print("2. sign in")
            print("3. Quit")
            user_choice = int(input("Choice : "))
            if user_choice == 1:
                username = self.create_account()
                if username != False:
                    self.create_password(username)
            elif user_choice == 2:
                username = input("Write your username : ")
                if os.path.exists(username):
                    if self.login(username):
                        small_flag = True
                        while small_flag:
                            print("1. Input information ")
                            print("2. Read information ")
                            print("3. Quit")
                            small_userchoice = int(input("Select option : "))
                            if small_userchoice == 1:
                                self.writing(username)
                            elif small_userchoice ==2:
                                self.reading(username)
                            else:
                                small_flag = False
                    else:
                        print("Wrong username or password")
                else:
                    print("TRY AGAIN")
            
            elif user_choice == 3:
                flag = False
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")



main = Manager()
main.running()