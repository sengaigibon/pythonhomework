import datetime

name = input('Introduce your name: ')
age = int(input('Introduce your age: '))

now = datetime.datetime.now()

yearTo100 = now.year + age

print ("Hey, %s, you have %d and you'll have 100 on year %d" % (name, age, yearTo100))
print ("Hey,", name ,", you have", age,"and you'll have 100 on year " + str(yearTo100))

# i = 0
# while i < age:
#     print('Name: ' + name)
#     i = i + 1
