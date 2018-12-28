import sys

def checkIfIsPrimeNumber(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    else:
        return True

if len(sys.argv) == 1:
    number = int(input('Give me a number: '))
else:
    number = int(sys.argv[1])

if checkIfIsPrimeNumber(number):
    print(str(number) + ' is prime')
else:
    print(str(number) + ' is not prime')