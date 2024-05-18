import random
#import the random module
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    #take the user input
    choice = int(input("Enter your choice: "))

    #OR is the short-circuit operator, if any condition is true
    #then it will return the True value. Now, let's loop until the
    #user inputs something invalid
    while choice > 3 or choice < 1:
        choice = int(input("Please, Enter a valid choice: "))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'
        
        print('User choice is \n', choice_name)
        print("Now, it's the Computer's turn...")

        #computer chooses randon number between 1 and 3
        #using randint Method

        comp_choice = random.randint(1, 3)

        #looping until computer's choice is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'
        
        print("Computer choice is \n", comp_choice_name)
        print(choice_name, "VS", comp_choice_name)

        #let's check for a draw
        if choice == comp_choice:
            print("It's a Draw", end="")
            result = "DRAW"
        #condition for winning
        if(choice == 1 and comp_choice == 2):
            print('Paper wins =>', end="")
            result = 'Paper'
        elif(choice == 2 and comp_choice ==1):
            print("Paper winds =>", end="")
            result = 'Paper'

        if(choice == 1 and comp_choice == 3):
            print('Rock wins =>\n', end="")
            result = 'Rock'
        elif(choice == 3 and comp_choice == 1):
            print('Rock wins =>\n', end="")
            result = 'Rock'

        if(choice == 2 and comp_choice == 3):
            print('Scissors wins =>', end="")
            result = 'Scissors'
        elif(choice == 3 and comp_choice == 2):
            print('Scissors wins =>', end="")
            result = 'Rock'

        #printing either user or computer wins or draws
        if result == 'DRAW':
            print('<== Its a tie ==>')
        if result == choice_name:
            print("<== User Wins ==>")
        else:
            print("<== Computer Wins ==>")
        print("Do you want to play again? (Y/N)")
        answer = input().lower()
        if answer == 'n':
            break

print("Thanks for playing")