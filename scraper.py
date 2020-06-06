import requests
from bs4 import BeautifulSoup
import pandas 
import numpy
import re

base_url = "https://www.goodreads.com/quotes/tag/"
tags = ['life','love','success']

'''
for tag in tags:`
    response = requests.get(base_url + tag)
    content = response.content
    filename = 'goodreads_' + tag + '.html'
    with open(filename, mode = 'wb') as file:
        file.write(response.content)
'''
def convert_html_to_soup(filename):
    '''Takes in an HTML file and turns it into soup with BeautifulSoup'''
    with open(filename, mode = 'rb') as file:
        soup = BeautifulSoup(file, features="html.parser")
    return soup

quote_block = soup.findAll(attrs={"class": "quoteText"})[0]
quote = re.findall(r'“(.*?)”', quote_block.text)[0]
dirty_author = quote_block.span.text
author = dirty_author.replace('\n','').strip(' ')



