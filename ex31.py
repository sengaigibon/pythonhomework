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
    wordFound = False
    maxGuesses = 6
    wordToGuess = pickRandomWord(filename)
    wordArray = list(wordToGuess)
    lettersUsed = []

    wordLen = len(wordToGuess)
    positionsGuessed = ['_' for x in range(wordLen)]

    print('Playing Hang Man!!')
    
    print('Guess your word >>> ')

    while maxGuesses:
        print(' '.join(positionsGuessed))
        letterVeredict = 'incorrect'
        letter = input('Give me one letter (%d times left): ' % maxGuesses).strip()
        letter = letter.upper()

        lettersUsed.append(letter)
        for index in range(wordLen):
            if wordArray[index] == letter:
                positionsGuessed[index] = wordArray[index]
                letterVeredict = 'correct'
                maxGuesses += 1

        print('%s was %s!' % (letter, letterVeredict))
        maxGuesses -= 1

        if not '_' in positionsGuessed:
            print('Congrats! You found the word: ')
            print(' '.join(positionsGuessed))
            wordFound = True
            break
        
    if not wordFound:
        print('Word was "%s". Better luck the next time... Keep trying! ' % wordToGuess)



