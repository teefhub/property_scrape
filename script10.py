import requests
from bs4 import BeautifulSoup
import itertools
import pandas as pd

def get_property(url, page):
    params = dict(page=page)
    response = requests.get(url=url, params=params)# will format `?page=#` to url
    c = response.content  # print(c) #html format content
    soup = BeautifulSoup(c, "html.parser")
    info_box = soup.find_all("div", {"class": "css-qrqvvg"})
    l = []
    d = {}
    for property in info_box:
        d['price'] = property.find("p", {"class": "css-mgq8yx"}).text

        d['address'] = property.find("a", {"class": "address is-two-lines css-1y2bib4"}).text.replace(u'\xa0', u' ')
        d['bedbathcar'] = property.find("div", {"class": "css-18biwo"}).text
        d['type'] = property.find("div", {"class": "css-11n8uyu"}).text
        l.append(d)
    return l
url = 'https://www.domain.com.au/sale/wentworth-point-nsw-2127/'
df = pd.DataFrame([])
for page in itertools.count(start = 1):
    list = get_property(url,page)
    if list:
        df.append(list)
    else:
        break
print(df)
#df.to_excel('data.xsxl', index=False)
