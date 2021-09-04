from bs4 import BeautifulSoup
import requests
from itertools import zip_longest

mxnum=''
def mxnum():
    r = requests.get(
        "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi")
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.findAll("div", {'class': '_2zg3yZ'}):
        mxnum = list(item.strings)[0].split(" ")[-1]
    return int(mxnum) + 1


mxnum = mxnum()


def Parse():
    with requests.Session() as req:
        names = []
        prices = []
        rating = []
        for num in range(1, mxnum):
            print(f"Extracting Page# {num}")
            r = req.get(
                f"https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page={num}")
            soup = BeautifulSoup(r.text, 'html.parser')
            for name in soup.find_all("div", {'class': '_3wU53n'}):
                names.append(name.text)
            for price in soup.find_all("div", {'class': '_1vC4OE _2rQ-NK'}):
                prices.append(price.text[1:])
            for rate in soup.find_all("div", {'class': 'hGSR34'}):
                rating.append(rate.text)
    for a, b, c in zip_longest(names, prices, rating):
        print("Name: {}, Price: {}, Rate: {}".format(a, b, c))


Parse()