#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

words = input('give me a string: ').replace(" ","")

strLen = len(words)
backCounter = strLen - 1
counter = 0

palindrome = False

while True:
    if words[counter] == words[backCounter]:
        counter = counter + 1
        backCounter = backCounter - 1
        if (counter == backCounter) or (backCounter < counter):
            palindrome = True
            break
    else:
        break

if palindrome:
    print(words + ' IS a palindrome')
else:
    print(words + ' IS NOT a palindrome')