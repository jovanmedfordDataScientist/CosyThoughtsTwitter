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

class Quote:
    def __init__(self,quote_block):
        self._text = None
        self._author = None
        self.quote_block = quote_block

    @property
    def text(self):   
        dirty_quote = self.quote_block.text
        match = re.search(r'“(.*?)”', dirty_quote)
        if (match):
            text = match.group(0).replace('“',"").replace('”',"")
        else:
            text = dirty_quote
        return text

    @property
    def author(self):
       dirty_author = self.quote_block.span.text
       return dirty_author.replace('\n','').strip(' ')


def extract_quotes(filename):
    soup = convert_html_to_soup(filename)
    quote_blocks = soup.findAll(attrs={"class": "quoteText"})
    for quote_block in quote_blocks:
        quote = Quote(quote_block)
        print(quote.text + "\n -" + quote.author + '\n\n')

extract_quotes(r'CosyThoughts\goodreads_life.html')

'''
souped = convert_html_to_soup('goodreads_love.html')
quote_block = souped.findAll(attrs={"class": "quoteText"})[0]
quote = re.findall(r'“(.*?)”', quote_block.text)[0]
dirty_author = quote_block.span.text
author = dirty_author.replace('\n','').strip(' ')

'''
