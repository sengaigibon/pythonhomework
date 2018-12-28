# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One resources/primenumbers.txt file has a list of all prime numbers under 1000, 
# and the other resources/happynumbers.txt file has a list of happy numbers up to 1000.

def getLinesAsList(filename):
    tmpFile = open(filename, 'r')

    lstLines = []
    line = tmpFile.readline().replace('\n','')
    while line:
        lstLines.append(line)
        line = tmpFile.readline().replace('\n','')

    tmpFile.close()
    return lstLines

if __name__ == "__main__":
    lstPrimeNums = getLinesAsList('resources/primenumbers.txt')
    lstHappyNums = getLinesAsList('resources/happynumbers.txt')

    lstPrimeAndHappy = [num for num in lstPrimeNums if num in lstHappyNums]

    print(lstPrimeAndHappy)
