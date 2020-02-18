import random

x = random.randint(0,20)

a = 1

#print(x)

print("Hello and welcome to Guess The Number!")
print("The computer has chosen a random integer between 0 and 20 and it is your job to guess it!")
print("What is your first guess?")

def guess(y):
    global a
    if y.isnumeric() == False:
        print("Sorry, that's not a integer! Please try again.")
        guess(input())
    if int(y) > 20 or int(y) < 0:
        print("Your guess must be an integer between 0 and 20! Please try again.")
        guess(input())
    if int(y) > x:
        print("Sorry, that's too high! Please try again.")
        a += 1
        guess(input())
    if int(y) < x:
        print("Sorry, that's too low! Please try again.")
        a += 1
        guess(input())
    

guess(input())

print("You got it! It took you " + str(a) + " goes!")

