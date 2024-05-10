
class Cipher:
    def __init__(self,id):
        self.id = id #key = id

    def encrypt(self,secret):
        result = []
        if(len(secret)!=len(self.id)):
            for i in range(len(secret)-len(self.id)):
                self.id = self.id + "A"
        for i in range(len(secret)):
            x = ord(secret[i])+ord(self.id[i]) % 26
            x = chr(x)
            result.append(x)
        return ("".join(result))
    
    def decrypt(self,reading):
        result = []
        if(len(reading)!=len(self.id)):
            for i in range(len(reading)-len(self.id)):
                self.id = self.id + "A"
        for i in range(len(reading)):
            x = ord(reading[i]) - ord(self.id[i]) % 26
            x = chr(x)
            result.append(x)
        return("".join(result))
