# This is a guess the number game
import random

guessesTaken = 0

print ('Hello, What is you name?')
myName = input ()

number = random.randint (1, 20)
print ('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range (6):
    print ('Take a guess.')
    guess = input ()
    guess = int (guess)

    if guess < number :
        print ('Your guess is too low.')

    if guess > number :
        print ('Your guess is too high.')

    if guess == number :
        break

if guess == number :
    guessesTaken = str (guessesTaken + 1)
    print ('Good job, ' + myName + '! You have guessed my number in ' + guessesTaken + ' guesses!')

if guess != number :
    number = str (number)
    print ('Nope. The number i was thinking of was' + number + '.')
