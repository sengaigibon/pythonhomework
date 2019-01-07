# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

var1 = int(input('Give me variable 1: ').strip())
var2 = int(input('Give me variable 2: ').strip())
var3 = int(input('Give me variable 3: ').strip())

ord = list([var1,var2,var3])
ord.sort()
print('Max is %d' % ord[2])