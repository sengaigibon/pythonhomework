import random
import datetime
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 999]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 
# Write this using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
now = datetime.datetime.now()
randSizeOfList = random.randint(10, now.second * 2)

a = []
for x in range(1, randSizeOfList):
    a.append(random.randint(1, 500))

randSizeOfList = random.randint(5, now.second * 2)

b = []
for x in range(1, randSizeOfList):
    b.append(random.randint(1, 500))

c = [x for x in a if x in b]
lenC = len(c)
d = [c[x] for x in range(lenC - 1) if c[x] != c[x + 1]]
if c[lenC - 1] != c[lenC - 2]: d.append(c[lenC - 1])

a.sort()
b.sort()
print(a)
print(b)
print('')
print(d)