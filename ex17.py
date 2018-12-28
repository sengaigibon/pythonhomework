# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the es.sott.net homepage

import requests
from bs4 import BeautifulSoup

url = 'https://es.sott.net'
r = requests.get(url)
rHtml = r.text

soup = BeautifulSoup(rHtml, "lxml")

for item in soup.find_all(class_='tbli'):
    print(item.a.string)