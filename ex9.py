# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

print ("Guessing Game One!")

games = 1
times = 0
randomToGuess = 0
scores = []

while True:
    
    times = times + 1
    if times == 1:
        randomToGuess = random.randint(0,10)

    guess = input('Guess my number (or type exit): ')
    
    if guess == 'exit': break
    guess = int(guess)

    if guess == randomToGuess:
        print("You found it!!! ")
        scores.append('[' + str(games) + ',' + str(times) + ']')
        times = 0
        games = games + 1
    elif guess < randomToGuess:
        print("Closer but too low")
    elif guess > randomToGuess:
        print("Closer but too high")

print('Your score (game, tries):')
print(scores)