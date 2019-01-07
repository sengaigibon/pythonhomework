# Hangman Part 1
# The task is to write a function that picks a random word from a list of words from the 'resources/sowpods.txt' dictionary.

import random

def pickRandomWord(filename):
    tmpFile = open(filename, 'r')

    lstLines = []
    line = tmpFile.readline().replace('\n','')
    while line:
        lstLines.append(line)
        line = tmpFile.readline().replace('\n','')

    tmpFile.close()
    last = len(lstLines) - 1
    return lstLines[random.randint(0, last)]




##########

if __name__ == "__main__":
    filename = 'resources/sowpods.txt'
    print(pickRandomWord(filename))