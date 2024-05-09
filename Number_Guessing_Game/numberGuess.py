"""Let's make a simple number guessing game 
that will take user inputs in a selected range"""
import random
import math

#Have user enter the lower number input first
lower = int(input("Enter Lower bound:- "))
#Now, have the user enter the upper number 
upper = int(input("Enter Upper bound:- "))

#Generate random numbers between the upper and lower numbers
x = random.randint(lower,upper)
print("\n\tYou've only ", 
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

#Initialize the number of guesses. Start by setting count to 0
count = 0 
#Use a while loop to calculate the minimum number of guesses dependent on range
while count < math.log(upper - lower + 1,2):
    count += 1

    #take input for guessing number
    guess = int(input("Guess a number:- "))

    #Condition testing
    if x == guess:
        print("Congratulations! You did it in ", 
              count, " tries")
        #once guess, break the loop
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

#If guessing is more than required guesses,
#show this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
              