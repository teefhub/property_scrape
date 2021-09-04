import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

def get_property():

    Numpage = 0

    for page in range(11):
        url = 'https://www.auhouseprices.com/sold/list/NSW/2127/Wentworth+Point/'
        response = requests.get(url=url+str(page))
        c = response.content
        soup = BeautifulSoup(c, "html.parser")
        all = soup.findAll("div", {"class": "caption"})

        price_list = []
        address_list = []
        bedroom_list=[]
        date_list = []
        complete_list = []
        next_page = soup.find('a', {'class': 'goto_nextpage'})
        print(next_page)
        if all != []:
            if next_page:
                Numpage += 1
                for item in all:
                    d={}
                    d["price"] = item.find("span", {"class": "pull-right"}).text
                    #price = d["price"]
                    #price_list.append(price)
                    d["address"] = item.find("h4").text
                    #address_list.append(address)
                    d["bed"]= item.find("big").text
                    #bedroom_list.append(bed)
                    d["date"] = item.find("li").text
                    #date_list.append(date)
                    #complete_list.append(price)
                    price_list.append(d)
        else:
            break
            sleep(randint(1, 2))
    print('You scraped {} pages'.format(Numpage))
    cols = ['Price', 'Address','Bed','Date']
    #convert list to data frame
    df = pd.DataFrame(price_list)
    print(df)
    timeD=time.strftime("%Y-%m-%d-%H%S",time.localtime())
    df.to_csv(timeD+'.csv', index=False)
    
get_property()


