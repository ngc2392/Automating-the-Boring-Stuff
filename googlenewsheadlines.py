#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

#Get news titles from google news, output a summary
import requests
from bs4 import BeautifulSoup
#this gets more than just title.  Figure out how to get just title
url='https://news.google.com/news/headlines?hl=en'
webpageText = requests.get(url)
soup = BeautifulSoup(webpageText.text, 'html.parser')
#print(soup.prettify())
headlines = soup.find_all('a',role="heading")
for headlineName in headlines:
    articleLink = headlineName["href"]
    #print("ALL HEADLINE: " + str(headlineName))
    #print("THE HEADLINE HAS AN aria-level value of " + headlineName["aria-level"])
    #print("HEADLINE OF A RELATED COVERAGE: " + headlineName.text)
    #print("LINK OF ABOVE HEADLINE: " + articleLink)


    if(headlineName["aria-level"] is "2"): #ignore 'RELATED COVERAGE'
        print("HEADLINE: " + headlineName.text)
        print("LINK OF ABOVE HEADLINE: " + articleLink)
    
        print(" ")
        
    print(" ")
        
        
#listens for input.  Type a number in and gives a summary of that article
# pass in a number and the word 'open' and it opens that link in a web browser
#figure out how to get just main headlines.  If user wants related coverage, type in 'e'
#get the weather
#save the weather images and print them to console
#local news also by typing local


