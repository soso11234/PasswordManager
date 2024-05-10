import os
class Id:
    def create_id(self,username):
        if os.path.exists(username):
            print("Already exist username.")
            return False
        try:
            with open(f'{username}','a',encoding ='utf-8')as f:
                print(f"Make {id} successfully")
                return True
        except Exception as e:
            print(f"Failed to create {username}:{e}")
            return False
    def check_id(self,username):
        try:
            with open(f'{username}','r',encoding= 'utf-8')as f:
                return True
        except Exception as e:
            print(f"Failed to find {username} : {e}")
            return False
