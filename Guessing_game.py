#Challenge 1
#Guessing game

import random

num = random.randint(1,10)

guess = ""

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    if guess>num:
        print("The number is too high. Try again!")
    if guess < num:
        print("The number is too low. Try again!")