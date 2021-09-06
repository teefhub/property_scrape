import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

def get_property():
    url = 'https://www.aupropertyreport.com/property-report/unit-13-21-27-meadow-cres-meadowbank-nsw-2114'
    response = requests.get(url=url)
    c = response.content

    soup = BeautifulSoup(c, "html.parser")
    print(soup)
    all_c = soup.findAll("div", {"class": "main-content "})
    #print(all_c)
    ls = []
    for item in all_c:
        print(item)
        d={}
        d["last_sold_price"] = item.find("div", {"class": "packages mixItUp"}).text
        ls.append(d)
    print(ls)

    
get_property()


