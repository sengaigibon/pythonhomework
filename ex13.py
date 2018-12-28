#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def sum(lst):
    return lst[0] + lst[1]

# pass-by-reference by default
def nextFibonnaci(lst):
    lst.append(sum(lst[:-3:-1]))

num = int(input('Give me a number:'))

if num == 0:
    fibon = []
if num == 1:
    fibon = [1]
else:
    fibon = [1,1]
    for x in range(2, num):
        nextFibonnaci(fibon)

print(fibon)