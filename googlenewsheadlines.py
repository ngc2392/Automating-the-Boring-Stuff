#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import requests
from bs4 import BeautifulSoup

url='https://news.google.com/news/headlines?hl=en'
text = requests.get(url)
soup = BeautifulSoup(text.text, 'html.parser')
print(soup.prettify())
headlines = soup.find_all('a',role="heading")
for headlineName in headlines:
    print(headlineName.text)

