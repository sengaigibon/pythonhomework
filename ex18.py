# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.

import random

def compareTwoNums(goal, test):
    result = [0,0]
    for i in range(0,4):
        if test[i] == goal[i]:
            result[0] += 1 #cows
        else:
            result[1] += 1 #bulls
    return result

def cowsAndBullsGame():
    numToGuess = str(random.randint(1000,9999))
    totalGuesses = 0

    print('Welcome to the Cows and Bulls Game!')

    while True:
        num = input('Enter a number: ')
        totalGuesses += 1

        arrCowsBulls = compareTwoNums(num, numToGuess)

        if arrCowsBulls[0] == 4:
            break
        else:
            print('Cows=%d | Bulls=%d' % (arrCowsBulls[0], arrCowsBulls[1]))

    print('Congrats! In %d guesses you found the secret number is: %s' % (totalGuesses, numToGuess))



if __name__ == "__main__":
    cowsAndBullsGame()


