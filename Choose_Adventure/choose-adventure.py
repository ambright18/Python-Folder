#A basic template of a choose your own adventure story that can be edited or even add more content.
name = input("Enter your name here: ")
print("Welcome to your custom adventure,", name)

answer = input("You wake up, lying in the middle of a dirt path going in two directions. Do you move forward or backward? ")

if answer.lower() == "forward":
    answer = input("You walk forward, travelling across a meadow with swaying colors of flowers against the wind. In the middle of the flower field, you come across a grand oak tree. Do you walk to the tree or pass it by? Type 'walk' to go to the tree or 'pass' to leave it behind: ")

    if answer == 'walk':
        print("You walk up to the mysterious tree, but a large branch suddenly falls on your head, ending your adventure forever...")
    elif answer == 'pass':
        print("You decide to continue walking forward, pass the large tree until you come across a stone bridge over a river.")
    else:
        print("Not a valid option, please try again.")

elif answer.lower() == "backward":
    answer = input("You turn around and head down the path, passing over rocky terrain and hills. You finally approach the beginning of a large forest. Do you wish to enter the forest or walk around it? Type 'enter' to go in or 'around' to walk around the forest: ")
    if answer == 'enter':
        print("You decide to venture into the deep forest, admiring the canopies of tall trees and the rays of sunshine peering through the branches. You notice the light landing directly over a small house in the middle of the woods...")
    elif answer == 'around':
        print("You decide to walk around the forest, but end up venturing deep into a harsh desert, void of all life and water. You walk for hours which turn into days until you collapse from the heat, ending your adventure...")
    else:
        print("Not a valid option, please try again.")
else:
    print("Not a valid option, please try again.")
