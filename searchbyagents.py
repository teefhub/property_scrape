import requests
import json
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
        #list.append(pid)
        d["status"] = r[i]["objective"]
        #list.append(status)
        d["price"]  = r[i]["priceDetails"]["displayPrice"]
        #list.append(price)
        d["address"]  = r[i]["addressParts"]["displayAddress"]
        #list.append(address)
        d["ptype"]  = r[i]["propertyTypes"]
        #list.append(ptype)
        d["bed"]  = r[i]["bedrooms"]
        #list.append(bed)
        d["bath"]  = r[i]["bathrooms"]
        #list.append(bath)
        d["car"]  = r[i]["carspaces"]
        #list.append(car)
        d["dateListed"]  = r[i]["dateListed"]
        #list.append(dateListed)
        d["link"]  = r[i]["seoUrl"]
        list.append(d)
        #print("for "+str(status)+"\n"+str(bed)+" bed "+str(bath)+" bath "+str(car)+" car\n"+str(address)+"\n"+str(dateListed)+"\n"+str(price)+"\n"+str(link)+"\n"+"=====================")
    #print("END OF LIST")
    #print(list)
    ls=[]
    for i in range(len(list)):
        ls.append(list[i]["pid"])
    #print(ls)
    return ls
    
get_property_info()

def export():
    data = get_property_info()
    #print(type(data))
    #print(data)
    df = pd.DataFrame(data,columns=["ID","Objective","Price","Address","Type","Bed","Bath","Car", "Date Listed","Link"])
    aid = api.id
    print(len(data))
    print(df)
    for index, row in df.iterrows():
        print(data[index]["pid"],data[index]["status"],data[index]["price"],data[index]["address"],
                       data[index]["ptype"],data[index]["bed"],
                       data[index]["bath"],data[index]["car"],
                       data[index]["dateListed"],data[index]["link"])
    #print(df)
    timeD=time.strftime("%Y-%m-%d-%H%S -",time.localtime())
    #df.to_csv(timeD+aid+'.csv', index=True)
    

#export()




