import random
import datetime

# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

finalList = []
for x in a:
    if x in b:
        if x not in finalList:
            finalList.append(x)
else: 
    print(finalList)

now = datetime.datetime.now()
randSizeOfList = random.randint(10, now.second * 2)

list1 = []
for x in range(1, randSizeOfList):
    list1.append(random.randint(1, 500))

randSizeOfList = random.randint(10, now.second * 2)

list2 = []
for x in range(1, randSizeOfList):
    list2.append(random.randint(1, 500))

print(list1)
print(list2)

finalList = []
for x in list1:
    if x in list2:
        if x not in finalList:
            finalList.append(x)
else: 
    print(finalList)

# after exercise 14
print(set([x for x in list1 if x in list2]))