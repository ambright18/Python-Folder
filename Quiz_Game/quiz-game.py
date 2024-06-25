#a quiz game implenenting the use of if else 
#statements, displaying how many questions the
#user got correct. Perfect for new beginners to python

print("Welcome to Alex's Computer Quiz Game!!")

playing = input("Would you like to take my quiz? ")


if playing.lower() != "yes":
    quit()
print("Time to play!!")
score = 0
bad_score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
else: 
    print("I'm sorry, that's incorrect :(")
    bad_score += 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!!")
    score += 1
else: 
    print("I'm sorry, that's incorrect :(")
    bad_score += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!!")
    score += 1
else: 
    print("I'm sorry, that's incorrect :(")
    bad_score += 1

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print("Correct!!")
    score += 1
else: 
    print("I'm sorry, that's incorrect :(")
    bad_score += 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!!")
    score += 1
else: 
    print("I'm sorry, that's incorrect :(")
    bad_score += 1

print("You got " + str(score) + " questions correct!")
print("You got " + str(bad_score) + " questions incorrect :(")
print("Total percentage is " + str((score/5) * 100) + "%")


