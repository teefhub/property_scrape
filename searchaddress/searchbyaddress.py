import requests
import json
import searchbyagents as agents
import openpyxl
import api_connection as api
import pandas as pd
import time

def get_property_info():
    id = api.id 
    response = requests.post(api.auth_url, data = {
                        'client_id':api.client_id,
                        'client_secret':api.client_secret,
                        'grant_type':'client_credentials',
                        'scope':api.scopes,
                        'Content-Type':'text/json'
                        })
    json_res = response.json()
    access_token=json_res['access_token']
    auth = {'Authorization':'Bearer ' + access_token}
    url = api.url_endpoint
    res1 = requests.get(url, headers=auth)
    r = res1.json()
    list = []
    for i in range(len(r)):
        d={}
        d["pid"] = r[i]["id"]
        list.append(d)
    ls=[]
    for i in range(len(list)):
        ls.append(list[i]["pid"])
    return ls
get_property_info()

def get_property():
    property_id = get_property_info()
    
    response = requests.post(api.auth_url, data = {
                        'client_id':api.client_id,
                        'client_secret':api.client_secret,
                        'grant_type':'client_credentials',
                        'scope':api.scopes2,
                        'Content-Type':'text/json'
                        })
    json_res = response.json()
    access_token=json_res['access_token']
    auth = {'Authorization':'Bearer ' + access_token}
    ls=[]
    for i in range(len(property_id)):
        url = api.url_endpoint2 + str(property_id[i])
        res1 = requests.get(url, headers=auth)
        r = res1.json()
        d={}
        d["saleMode"]=r["saleMode"]
        d["displayPrice"]=r["priceDetails"]["displayPrice"]
        d["displayAddress"]=r["addressParts"]["displayAddress"]
        d["streetNumber"] = r["addressParts"]["streetNumber"]
        d["street"] = r["addressParts"]["street"]
        d["suburb"] = r["addressParts"]["suburb"]
        d["postcode"] =r["addressParts"]["postcode"]
        d["bathrooms"] = r["bathrooms"]
        d["dateListed"] = r["dateListed"]
        d["seoUrl"] = r["seoUrl"]
        ls.append(d)
    df = pd.DataFrame(ls)
   
    print(df)
    
    timeD=time.strftime("%Y-%m-%d-%H%S",time.localtime())
    df.to_excel(r'searchaddress/'+timeD+'-searchbyaddress.xlsx', index = False)
get_property()