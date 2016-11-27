# Guess the number game
import random

secretNumber = random.randint(1, 20) #between 1 and 20
print('I am thinking of a number between 1 and 20.')

# Ask the palyer to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input()) # take the input as an int

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this is the correct condition

if guess == secretNumber: # the correct condition
    print('Good job! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
