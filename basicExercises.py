#Exercise 1: Print first 10 natural numbers using While Loop
"""index = 1
while index <=10:
    print(index)
    index += 1 """

#Exercise 2: Print the following Pattern 
#Decide the row count (pattern should contain 5 rows)
#row = 5
#start: 1
#stop: row+1 (range never include stop number in result)
#step: 1
#run loop 5 times
"""for i in range(1, row + 1, 1):
    #Run inner loop i+1
    for j in range(1, i + 1):
        print(j, end=' ')
        #empty line after each row
    print("")"""

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
#First, store sum of all numbers
"""sum = 0
number = int(input("Enter a number: "))
#run loop number of times
#stop: n+1 (because range never include stop number in result)
for index in range(1, number + 1, 1):
    # add curetn number to sum variable
    sum += index
print("\n")
print("Sum is: ", sum)"""

#Exercise 4: A program to print multiplication table of a given number

"""number = int(input("Enter a number: "))
#stop: 11 (because range never include stop number in result)
#run loop 10 times
for index in range(1, 11, 1):
    #2 *index (current number)
    product = number * index
    print(product)"""

#Exercise 5: Display numbers from a list using loop
"""numbers = [12, 75, 150, 180, 145, 525, 50]
#iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    #check if number is divisible by 5
    elif item % 5 == 0:
        print(item)"""

#Exercise 6: Count the total number of digits in a nubmer
""" num = int(input("Enter a number here: "))
count = 0
while num != 0:
    #floor division
    # to reduce the last digit from number
    num = num // 10

    #increment counter by 1
    count = count + 1
print("Total digits are: ", count)"""

#Exercise 7: Print the following pattern from Exercise 2 in reverse order
""" num = 5
k = 5
for index in range (0, num + 1):
    for j in range(k-index, 0, -1):
        print(j, end=' ')
    print() """

#Exercise 8: Print a list array in reverse order using a loop
""" list1 = [10, 20, 30, 40, 50]
#reverse list
new_list = reversed(list1)
#iterate reversed list
for item in new_list:
    print(item) """

#Exercise 9: Display numbers from -10 to -1 using for loop
"""for num in range (-10, 0 ,1):
    print(num)"""

#Exercise 10: Use else block to display a message "Done" after
#successful execution of for loop
"""for index in range(5):
    print(index)
else: 
    print("Done!")"""

#Exercise 11: Write a program to display all prime numbers within a range
"""start = 25
end = 50
print("Prime nubmers between", start, "and", end, "are: ")

for num in range(start, end + 1):
    #all prime numbers are greater than 1
    #if number is less than or equal to 1, it is not prime
    if num > 1:
        for index in range(2, num):
            #check for factors
            if(num % index) == 0:
                #not a prime number so break inner loop and
                #look for next number
                break
        else: 
            print(num) """

#Exercise 12: Display the Fibonacci series up to 10 terms
#first, lets have the user enter 2 numbers
"""num1 = int(input("Enter first Number here: "))
num2 = int(input("Enter Second Number here: "))
print("Fibonacci Sequence: ")
#run the loop 10 times
for index in range(10):
    #print next number of a series
    print(num1, end=" ")
    #add last two numbers to get a number
    result = num1 + num2
    #Update values
    num1 = num2
    num2 = result """

#Exercise 13: Find the factorial of a given number
"""num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative nubmers")
elif num == 0:
    print("The factorial of 0 is 1")
else: 
    #run loop 5 times
    for index in range(1, num + 1):
        #multiply factorial by current number
        factorial = factorial * index
    print("The factorial of", num, "is", factorial)"""







