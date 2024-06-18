import string
import random

print("Alex's Python Password Generator")

length = int(input('Enter password length: '))

print('''
Choose character set for password from these:
      1. Digits
      2. Letters
      3. Special Characters
      4. Exit

''')

characterList = ""

while(True):
    choice = int(input("Pick a number: "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please, pick a valid option")

password = []

for index in range(length):
    randomChar = random.choice(characterList)

    password.append(randomChar)


print("The random password is " + "".join(password))