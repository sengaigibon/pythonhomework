# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = input('give me a number: ')

multipleOf2 = int(number) % 2

if multipleOf2 == 0:
    print(number + ' is an even number (par)')
else: 
    print(number + ' is an odd number (impar)')

multipleOf4 = int(number) % 4

if multipleOf4 == 0:
    print(number + ' is multiple of 4')
else: 
    print(number + ' is not multiple of 4')

divisor = input('give me a divisor: ')
dividendo = input('give me a dividendo: ')

if int(dividendo) % int(divisor):
    print(dividendo + '/' + divisor + ' divides evenly')
else: 
    print(dividendo + '/' + divisor + ' divides oddly')