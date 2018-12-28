# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 
# I have a resources/names.txt file for you, if you want to use it!

# Extra:
# Instead of using the .txt file from above (or instead of, if you want the challenge), take resources/training.txt file, 
# and count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. 
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. 

def solution1():
    fileName = '/Users/javier/workspace/python/resources/names.txt'
    namesFile = open(fileName,'r')

    names = {}
    line = namesFile.readline().replace('\n','')
    while line:
        if line in names:
            names[line] += 1
        else:
            names[line] = 1
        line = namesFile.readline().replace('\n','')
    
    namesFile.close()
    print(names)


def solution2():
    #format: /a/abbey/sun_ajgccggyendxydwa.jpg
    fileName = '/Users/javier/workspace/python/resources/training.txt'
    dataFile = open(fileName,'r')

    categories = {}
    cat = dataFile.readline()
    while cat:
        cat = cat.split('/')
        cat = cat[2]
        if cat in categories:
            categories[cat] += 1
        else:
            categories[cat] = 1
        cat = dataFile.readline()
    
    dataFile.close()
    for item, val in categories.items():
        print(item + ' >> ' + str(val))
    print(str(len(categories)) + ' categories in total')
    #print(categories)


if __name__ == "__main__":
    solution1()
    solution2()