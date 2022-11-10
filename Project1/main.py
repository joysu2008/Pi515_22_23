# Copyright 2022 PI515

import random

keepAsking = True
while keepAsking == True:
    num = input('Type a number for an upper bound: ')
    if num.isdigit():
        print("Let's play!")
        num = int(num)
        keepAsking = False
        # something about the loop condition
    else:
        print("Invalid input. Try again.")

secret = random.randint(1, num)
guess = None
count = 0

while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)
        count = count + 1
    if guess == secret: # can't always be wrong
        print("You got it!")
    else:
        print("Try again.")

if count == 1:
    print("It took you", count, "guess!")
else:
    print("It took you", count, "guesses!")
