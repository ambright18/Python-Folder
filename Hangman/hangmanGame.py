import random

hangManPics = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']

#let's make a hangman game using Python!!

#first, let's create an array of random words and store them in a string variable

words = '''apple cantaloupe banana strawberry pineapple 
pear orange cherry grape fig kiwi lemon lime mango 
tangarine watermelon peach plum'''.split()

#let's start by creating a function to return a random string from the passed list of strings.
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangManPics[len(missedLetters)])
    print()
    
    print("Missed Letters:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
        
    print()
    
    blanks = '_' * len(secretWord)
    
    for index in range(len(secretWord)): #replace blanks with correctly guessed letters
        if secretWord[index] in correctLetters:
            blanks = blanks[:index] + secretWord[index] + blanks[index+1:]
    for letter in blanks:
            print(letter, end=' ')
            print()
            
# function for getGuess will go here
def getGuess(alreadyGuessed):
     #return the letter to the player entered. This function makes sure the player entered a single letter and not something else.
     while True:
          print("Guess a letter.")
          guess = input()
          guess = guess.lower()
          if len(guess) != 1:
               print("Please enter a single letter.")
          elif guess in alreadyGuessed:
               print("You've already guessed that letter. Choose again.")
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
               print("Please, enter a LETTER.")
          else:
               return guess

#function for playAgain goes below
def playAgain():
     #this function returns True if the player wants to play again
     print("Do you want to play again? (yes or no)")
     return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
     displayBoard(missedLetters, correctLetters, secretWord)
     
	 #let the player enter a letter
     guess = getGuess(missedLetters + correctLetters)
     
     if guess in secretWord:
          correctLetters = correctLetters + guess
          
		  #check if the player has won
          foundAllLetters = True
          for index in range(len(secretWord)):
               if secretWord[index] not in correctLetters:
                    foundAllLetters = False
                    break
          if foundAllLetters:
               print("Yes! The secret word is " + secretWord + " You Won!!")
               gameIsDone = True
          else:
               missedLetters = missedLetters + guess
               
			   #check if player has guessed too many times and lost.
               if len(missedLetters) == len(hangManPics) - 1:
                    displayBoard(missedLetters, correctLetters, secretWord)
                    print('You have run out of guesses!\nAfter ' + 
                        str(len(missedLetters)) + ' missed guesses and ' +
                        str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                    gameIsDone = True
          #ask the player if they want to play again(but only if game is finished)
          if gameIsDone:
               if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False 
                    secretWord = getRandomWord(words)
               else:
                    break
                    
                
          
     
          
