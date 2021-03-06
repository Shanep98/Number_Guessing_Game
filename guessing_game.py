count = 0
play = 0
guess = 42


import sys

import time

import random


print("Luck is defined as a force that brings good fortune or adversity")
time.sleep(1.5)
print("People associate luck with probability or chance.")


test = input("Would you like to test your luck with a guessing game?(yes/no)  ")
test = test.lower()
while test != 'yes':
    if test == 'no':
        sys.exit("I understand then. Better to not tempt your luck.")

    else:
        print("Please just answer the question with a 'yes' or a 'no'")
        test = input("Would you like to test your luck with a guessing game?(yes/no)  ")
        continue


print("Great. Let's start with your name....")
time.sleep(1)
player_name = input("What is your name human?  ")
print("Okay {}, this is a simple game. I am thinking of a number between 1-10".format(player_name))

num = random.randint(1, 10)
while num != guess:
    try:
        guess = int(input("What number am I thinking of?  "))
    except ValueError:
        print("Please enter a number.  ")
    if guess < 1:
        print("Please enter a number between 1 and 10"  )
        continue
    if guess > 10:
        print("Please enter a number between 1 and 10"  )
        continue
    if num > guess:
        print("Its not that one. Your guess is lower than the number I am thinking off, try again.")
        count += 1
        continue
    if num < guess:
        print("Its not that one. Your guess is higher than the number I am thinking off, try again.")
        count += 1
        continue
    if guess == num:
        count += 1
        break

print("Great job {}, you got it right!! It only took you {} guess(es)!".format(player_name, count))
print("Thank you for playing.")
