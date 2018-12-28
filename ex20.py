# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

import random
import datetime


def exists(numList, num):
    if(num in numList):
        return True
    return False

def binSearch(numList, num):
    mid = int(len(numList) / 2)
    if num == numList[mid]:
        return True
    if mid == 0:
        return False
    elif num < numList[mid]:
        return binSearch(numList[:mid], num)
    elif num > numList[mid]:
        return binSearch(numList[mid+1:], num)
    return False


if __name__ == "__main__":
    
    # randList = [random.randint(1, 500) for x in range(1, random.randint(10, datetime.datetime.now().second * 2))]
    randList = [6, 10, 11, 15, 22, 45, 57, 62, 65, 95, 100, 102, 136, 140, 141, 172, 177, 186, 223, 235, 238, 245, 271, 289, 309, 322, 327, 361, 372, 387, 404, 412, 414, 422, 440, 452, 467, 492, 497]
    num = int(input("Give me a number: "))

    # randList.sort()
    print(randList)
    if (binSearch(randList, num)):
        print('Exists')
    else:
        print('Not in list')

    print('LOL')