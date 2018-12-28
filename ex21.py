# Take the code from the How To Decode A Website exercise and instead of printing the results to a screen, write the results to a txt file. 
# In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup 

def getContents(tree, printScr = True, outFile = None):
    for tag in tree:
        if(hasattr(tag, "children")):
            for child in tag.children:
                if(hasattr(child, "contents") and len(child.contents) > 1):
                    getContents(child, printScr, outFile)
                else:
                    if printScr:
                        print(child.string)
                    else:
                        outFile.write(child.string + "\n")
        else:
            if printScr:
                print(tag.string)
            else:
                outFile.write(tag.string + "\n")


if __name__ == "__main__":
    name = input('Write a name for your file: ')

    url = "https://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    response = requests.get(url)
    rawHtml = response.text

    soup = BeautifulSoup(rawHtml, "lxml")

    openFile = open(name, 'w')

    openFile.write(soup.find(class_='hed').text + "\n" + "\n")
    openFile.write(soup.find(class_='dek').span.text + "\n" + "\n")

    getContents(soup.find_all('p'), False, openFile)

    openFile.close()