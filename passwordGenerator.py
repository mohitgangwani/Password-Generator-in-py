import random as r
import string as s
class generatePassword:
    lowerCase = s.ascii_lowercase
    upperCase = s.ascii_uppercase
    numbers = [i for i in range(10)]
    specialChars = [ch for ch in "./<>?;:\"'`!@#$%^&*()[]{}_+=|-"]
    weightList = []
    def __init__(self,complexity,length):
        self.complexity = complexity
        self.length = length

    def setWeight(self):
        if self.complexity == 1:
            self.weightList.extend(['L' for i in range(r.randint(2,6))])
            self.weightList.extend(['U' for i in range(r.randint(1,3))])
            self.weightList.extend(['N' for i in range(r.randint(1,2))])
            self.weightList.extend("S"  for i in range(1))
            print(self.weightList)

        if self.complexity == 2:
            self.weightList.extend(['L' for i in range(r.randint(2,5))])
            self.weightList.extend(['U' for i in range(r.randint(1,3))])
            self.weightList.extend(['N' for i in range(r.randint(1,2))])
            self.weightList.extend(['S' for i in range(r.randint(1,2))])
            print(self.weightList)
        
        if self.complexity == 3:
            self.weightList.extend(['L' for i in range(r.randint(1,2))])
            self.weightList.extend(['U' for i in range(r.randint(1,2))])
            self.weightList.extend(['N' for i in range(r.randint(1,4))])
            self.weightList.extend(['S' for i in range(r.randint(2,4))])
            print(self.weightList)

    def createPassword(self):
        createdPassword = ''
        j = ''
        self.setWeight()
        for i in range(self.length):
            j = r.choice(self.weightList)
            if j == 'L':
                print("[INFO] Generated Char")
                createdPassword += r.choice(self.lowerCase)
            elif j == 'U':
                print("[INFO] Generated Upper Char")
                createdPassword += r.choice(self.upperCase)
            elif j == 'N':
                print("[INFO] Generated Digit")
                createdPassword += str(r.choice(self.numbers))
            elif j == 'S':
                print("[INFO] Generated Special")
                createdPassword += r.choice(self.specialChars)
        print(createdPassword)
# o1 = generatePassword(1,4)
# o2 = generatePassword(2,5)
# o1.createPassword()
# o2.createPassword()
o3 = generatePassword(3,16)
o3.createPassword()
