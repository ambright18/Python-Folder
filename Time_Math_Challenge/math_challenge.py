import random 
import time

#lets create an array of the operators used for this project
operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10 #this will be the total number of problems

#the function below will generate a random math problem along with the operator used
def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press enter to start.")
print("---------------------")
start_time = time.time()

#below is how we'll arrange the math question along with the timer to see how long it takes the user to finish
for i in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2) #this calculates the total number of seconds it took to complete

print("---------------------")
print("Nice work! You finished in", total_time, "seconds!")
    
