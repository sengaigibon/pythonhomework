# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def setFromList(lst):
    return list(set(lst))

def removeDuplicates(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

def remDup(lst):
    res = []
    for i in set(lst):
        res.append(i)
    return res

lstDups = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
print(setFromList(lstDups))
print(removeDuplicates(lstDups))
print(remDup(lstDups))