# modules 
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from datetime import datetime

# variables
URL = 'YOUR_URL'
now = datetime.now()
date = now.strftime("%d_%m_%Y %H_%M_%S")

file1 = open("{date}.txt","w")
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)
        file1.write(data)

parser = MyHTMLParser()
page = requests.get(URL).text

soup = BeautifulSoup(page, "html.parser")

def parse_data():
    for row in soup.find_all("tr"):
        cells = str(row.find_all("td"))
        parser.feed(cells)

parse_data()



