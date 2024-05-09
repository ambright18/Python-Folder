"""Let's build a word guessing game using
Python's random module"""

import random

name = input("What is your name? ")

print("Good luck, ", name, "!")

#now, let's creat an array holding some words
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'sunshine', 'player', 'water', 'fire', 
         'earth', 'wind', 'dune']

#Let's create a function that will choose one random word from the array

word = random.choice(words)

print("Guess the characters")

guesses = ''

#Set the number of turns the player has
turns = 10

while turns > 0:
    #set the number of failed attempts to 0
    failed = 0
    #take characters from the input one at a time
    for char in word:
        #compare that character with the one in guesses
        if char in guesses:
            print(char, end=" ")
        else: 
            print("_")
            #for every failed attempt, 1 will be incremented
            failed += 1
    if failed == 0:
        #user will win the game if failure is 0
        print("You Win!!")

        #print the correct word
        print("The word is: ", word)
        break

    #if the user has entered the wrong alphabet, then it ask again
    print()
    guess = input("guess a character: ")

    #every input character will be stored in guesses
    guesses += guess

    #chekc input with character in word
    if guess not in word:
        turns -= 1

        print("Wrong!!")


        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You lose!!")