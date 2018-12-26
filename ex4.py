# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

number = int(input('give me a number: '))

tests = range(2, number + 1)

divisors = []

for x in tests:
    if(number % x == 0):
        divisors.append(x)
else:
    print(divisors)