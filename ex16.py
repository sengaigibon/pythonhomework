# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import datetime
import random

symbols = [['8','!','@','#','$','%','7'],['&','*','(',')','-','_','='],['+','/','"',':',';',',','.'],['?','a','b','c','d','e','f'],['g','h','i','j','k','l','m'],['n','ñ','o','p','q','r','s'],['t','u','v','w','x','y','z'],['9','1','2','3','4','5','6']]

words = ['Andén','Escafandra','Medir','Tótem','Fango','Velas','Congelar','Uvas','Diente','Horrible','Cautivo','Arrastrar','Frotar','Silo','Cucharón','Pañales','Asistencia','Transpiración','Láser','Zambullir','Torneo','Grasa','Aflojar','Novedad','Colmillos','Pinchar','Mozo','Faja','Cuarteto','Montura','Flojear','Saludar','Polen','Tubo','Padrastro','Escalpelo','Volar','Cuarteto','Unicornio','Talar']


def randomPass(passLenght = 10):
    pwd = ''
    fWord = words[random.randint(0,len(words)-1)]
    fWord = fWord[:10]
    randPos = [random.randint(0,passLenght), random.randint(0,passLenght)]

    for x in range(passLenght):
        if x in randPos:
            pwd += str(random.randint(0,9))
            continue 
        if random.randint(0,1):
            pwd += symbols[random.randint(0,6)][random.randint(0,6)]
        elif x >= len(fWord):
            pwd += symbols[random.randint(0,6)][random.randint(0,6)]
        else: 
            pwd += fWord[x] 
    else: 
        pwdLst = list(pwd)
        for x in range(len(pwdLst)):
            if(pwdLst[x].isalpha()):
                pwdLst[x] = pwdLst[x].upper()
                break
    
    return ''.join(pwdLst)

def readablePass():
    start = symbols[random.randint(0,6)][random.randint(0,6)]
    fWord = words[random.randint(0,len(words)-1)]
    if(start.isdigit()):
        mid = symbols[random.randint(0,6)][random.randint(0,6)]
    else:
        mid = str(random.randint(0,9)) + symbols[random.randint(1,2)][random.randint(0,6)]
    sWord = words[random.randint(0,len(words)-1)]
    end = str(random.randint(10,99))

    return (start + fWord + mid + sWord + end)



print('Random password generator')
type = 'c'
while not type.isdigit():
    type = input('Level of randomness: 1) Completely random, 2) Easy to remember: ')

type = int(type)
if type == 1:
    print(randomPass())
elif type == 2:
    print(readablePass())