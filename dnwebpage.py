#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import requests
from bs4 import BeautifulSoup
#pip3.5 install beautifulsoup4

res = requests.get('https://www.washingtonpost.com/news/post-politics/wp/2017/10/08/trump-administration-releases-hard-line-immigration-principles-threatening-deal-on-dreamers/?utm_term=.aa022aa887ca')
type(res)
res.status_code == requests.codes.ok
len(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find_all('p'))
#print(soup.prettify())
#print(res.text)
#print(res.text[:10000000])
