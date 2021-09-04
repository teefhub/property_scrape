
# Importing the libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Creating the requests object
# headers is used because some webpages don't like scripts sometimes So adding a header allows the script to impersonate a web browser
r= requests.get("https://www.realestate.com.au/sold/in-wentworth+point,+nsw+2127/list-1?includeSurrounding=false&source=refinement", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# Storing the content (HTML code) of website
#c= r.content
# Create BeautifulSoup object
#soup= BeautifulSoup(c, "html.parser")
# Extracting all the div elements containing property data
#all= soup.find_all("div",{"class":"residential-card__content"})
#find pricess
#all[0].find("span",{"class":"property-price"})

# To get the page number of webpages
# css-1oil53x - error list index out of range
#page_nr= BeautifulSoup.find_all("a",{"class":"pagination__link rui-button-brand"})[-1].text
#print(page_nr,"number of pages were found")

list = []
base_url = "https://www.realestate.com.au/sold/in-wentworth+point,+nsw+2127/list-1?includeSurrounding=false&source=refinement"
for page in range(0, 20):
    print()
    r = requests.get(base_url + str(page) + ".html")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"residential-card__content"})
    for item in all:
        d = {}
        d["Price"] = item.find("span", {"class": "property-price"})
        d["Address"] = item.find("h2", {"class": "residential-card__address-heading"})
        d["Beds"] = item.find_all("li", {"class": "general-features__icon general-features__beds"})
        d["Type"] = item.find("div", {"class": "css-11n8uyu"})
        d["Size"] = item.find("span",{"class": "property-size__icon property-size__building"})
        d["Date"] = item.find("span").find("Sold").text()

        list.append(d)
        print(d)