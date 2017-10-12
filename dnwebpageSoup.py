#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

#this will get romeo and juliet using beatiful soup

import requests
from bs4 import BeautifulSoup
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


url='http://www.gutenberg.org/cache/epub/1112/pg1112.txt'
webpageText = requests.get(url)
soup = BeautifulSoup(webpageText.text, 'html.parser')
print(soup.prettify())
