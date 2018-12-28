# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

import random
import datetime

def getFirstAndLast(lst):
    return [lst[0], lst[-1]]

a = [random.randint(1, 500) for x in range(1, random.randint(10, datetime.datetime.now().second * 2))]

print(a)
print(getFirstAndLast(a))