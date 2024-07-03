import random
#PIG is a type of dice game, so we'll create a roll function based of that

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
# let's now get the number of players from the user input
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

#this section controls the main mechanics of the dice game
while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            #if they enter anything other than 'y' it will end their turn and start
            #the next players turn
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done.")
                current_score = 0
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)
        
        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])
        
#sum up the total score and determine which player is the winner
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("\nPlayer number", winning_index + 1, "is the winner with a score of: ", max_score)