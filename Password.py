from Cipher import Cipher
from Id import Id
from Map import Map
class Password:
    def create_password(self,username):
        code = Map()
        code = code.password_drawing()
        cipher = Cipher(username)
        passcode_str = ''.join(str(x) for x in code)
        password = cipher.encrypt(passcode_str)
        print(password,'password')
        try:
            with open(f'{username}', 'a', encoding='utf-8') as f:
                f.write(str(password) + '\n')
            return True
        except FileNotFoundError:
            print("Can't find the username")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def match_password(self, username):
        id_instance = Id() 
        code = Map()
        code = code.password_drawing()
        cipher = Cipher(username)
        passcode_str = ''.join(str(x) for x in code)
        password = cipher.encrypt(passcode_str)
        print(password)
        if id_instance.check_id(username):
            try:
                with open(f'{username}', 'r', encoding='utf-8') as f:
                    saved_password = f.readline().strip()
                    if saved_password == password:
                        print("true")
                        return True
                    else:
                        print(saved_password)
                        print('Fasle')
                        return False
            except FileNotFoundError:
                print("Can't find the username")
                return False
            except Exception as e:
                print(f"Error: {e}")
                return False
        else:
            print("Can't find the username")
            return False
