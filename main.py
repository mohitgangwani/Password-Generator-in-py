from decimal import DecimalTuple
import passwordGenerator as passGen
from cryptography.fernet import Fernet 
import clipboard as cp
import os.path as path
import os
class Main:
    def __init__(self):
        if not path.exists('./KJSbxXJBfS.key'):
            self.setKey()
        while True:
            try:
                choice = int(input("Select Action:\n1. Create New Password\n2. Read Saved Password\n3. Exit\n"))
                if choice == 1:
                    self.getInput()
                    continue
                elif choice == 2:
                    self.getPasswords()
                    continue
                elif choice == 3:
                    break
            except ValueError:
                print("Please Enter a number input")
                continue


    def getInput(self):
        while True:
            try:
                self.length = int(input("Enter the Length of the Password: "))
            except ValueError:
                continue
            break
        
        while True:
            try:
               self.complexity = int(input("Enter the Complexity of the Password (Between 1 and 3): "))
            except ValueError:
                continue
            if(self.complexity < 1 or self.complexity > 3):
                print("Please Enter a value between 1 and 3")
                continue
            break

        while True:
            self.id = input("Enter the ID for the password (i.e. Any website name): ")
            self.id.strip()
            if(len(self.id) < 2 or len(self.id) > 20):
                print("The Minimum limit of the ID is 2, please enter the ID again")
                continue
            break
            
        while True:
            self.description = input("Enter the Description for the Password (Press enter if you want to skip): ")
            self.description.strip()
            if(self.description == ''):
                break
            if(len(self.description) < 2 or len(self.description) > 50):
                print("The Minimum limit of the Description is 2, please enter the Description again")
                continue
            break
        generatedPassword = passGen.generatePassword(self.complexity,self.length)
        self._generatedUserPassword = generatedPassword.createPassword()
        print(f"Your password is: {self._generatedUserPassword}")
        cp.copy(self._generatedUserPassword)
        while True:
            try:
                self.userChoice = input("Do you want to save the Generated Password? (y/n): ").strip().lower()[0]
            except:
                continue
            break

        if self.userChoice == 'y':
            self.savePassword()

    def getPasswords(self):
        key = self.getKey()
        fernet = Fernet(key)
        file = open('XvfentS.sdvx','rb')
        while True:
            line = file.readline()
            if(line == b""):
                break
            decryptPasswords = fernet.decrypt(line)
            decryptPasswords = decryptPasswords.decode()
            print(decryptPasswords)
        
    
    def savePassword(self):
        if not path.exists('./XvfentS.sdvx'):
            with open('XvfentS.sdvx','w') as file:
                pass
            os.system("attrib +h " + "XvfentS.sdvx")
            file.close()
        key = self.getKey()
        fernet = Fernet(key)
        file = open('XvfentS.sdvx','ab')
        encryptedText = fernet.encrypt(f"ID: {self.id}\nDescription: {self.description}\nPassword: {self._generatedUserPassword}\n\n".encode())
        file.write(encryptedText)
        file.write("\n".encode())

    def setKey(self):
        key = Fernet.generate_key()
        key = key.decode()
        # print(key)
        shiftedKey = ''
        for i in key:
            shiftedKey += chr(ord(i)+5)
        # print(shiftedKey)
        shiftedKey = shiftedKey.encode()
        with open("KJSbxXJBfS.key","wb") as file1:
            file1.write(shiftedKey)
        
        os.system("attrib +h " + "KJSbxXJBfS.key")
    
    def getKey(self):
        with open("KJSbxXJBfS.key","rb") as file1:
            shiftedKey = file1.read()
        shiftedKey = shiftedKey.decode()
        # print(shiftedKey)
        unshiftedKey = ''
        for i in shiftedKey:
            unshiftedKey += chr(ord(i)-5) 
        return unshiftedKey
        
userInput = Main()
