import random

#the randrange() function generates a random within the specified range

num = random.randrange(10000, 100000)

enteredNum = int(input("Guess the 5 digit number: "))

#let's create a condition to test the equality of the guess made and terminates if true
if(enteredNum == num):
    print("Wonderful! You guessed the number in just 1 try! You're a Mastermind!!")
else:
    ctr = 0
    #create a ctr variable. It will keep count of the number of tries the player made

    while (enteredNum != num):
        ctr += 1
        count = 0

        enteredNum = str(enteredNum)
        num = str(num)
        correct = []

        for index in range(0, 4):
            if(enteredNum[index] == num[index]):
                count += 1
                correct.append(enteredNum[index])
            else:
                continue
        if(count < 4) and (count != 0):
            print("Not quite. However, you did get ", count, " digit(s) correct!")
            print("Also, these numbers in your input were correct.")

            for k in correct:
                print(k, end=' ')

                print('\n')
                print('\n')
                enteredNum = int(input("Enter your next choice of numbers: "))
        elif(count == 0):
            print("None of the numbers in your input match.")
            enteredNum = int(input("Enter your next choice of numbers: "))

    if enteredNum == num:
        print("You've become a Mastermind!!")
        print("It took you only ", ctr," tries.")

