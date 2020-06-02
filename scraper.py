import requests
from bs4 import BeautifulSoup
import pandas 
import numpy


base_url = "https://www.goodreads.com/quotes/tag/"
tags = ['life','love','success']

for tag in tags:
    response = requests.get(base_url + tag)
    content = response.content
    filename = 'goodreads_' + tag
    with open(filename, mode = 'wb') as file:
        file.write(response.content)