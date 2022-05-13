import passwordGenerator as passGen
import cryptography as crypt
import clipboard as cp
class Main:
    # id, desc, length, complexity
    def getInput(self):
        while True:
            try:
                self.length = int(input("Enter the Length of the Password: "))
            except ValueError:
                continue
            break
        
        while True:
            try:
               self.complexity = int(input("Enter the Complexity of the Password(Between 1 and 3): "))
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
            self.description = input("Enter the Description for the password (Press enter if you want to skip): ")
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


    def savePassword(self):
        file = open('XvfentS.txt','a')
        file.write(f"ID: {self.id}\nDescription: {self.description}\nPassword: {self._generatedUserPassword}\n\n")

userInput = Main()
userInput.getInput()
