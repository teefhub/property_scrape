import requests
import json
import searchbyagents as agents
import api_connection as api
import pandas as pd



def get_property():
    property_id = agents.get_property_info()
    #post When you send some data on server then use post methods
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
    salemode=[]
    priceDetails=[]
    address=[]
    streetNumber=[]
    street=[]
    suburb=[]
    postcode=[]
    bathrooms=[]
    dateListed=[]
    seoUrl=[]
    for i in range(len(property_id)):
        print(property_id[i])
        url = api.url_endpoint2 + str(property_id[i])
        res1 = requests.get(url, headers=auth)
        r = res1.json()
        print(r)
        salemode.append(r["saleMode"])
        priceDetails.append(r["priceDetails"]["displayPrice"])
        address.append(r["addressParts"]["displayAddress"])
        streetNumber.append(r["addressParts"]["streetNumber"])
        street.append(r["addressParts"]["street"])
        suburb.append(r["addressParts"]["suburb"])
        postcode.append(r["addressParts"]["postcode"])
        bathrooms.append(r["bathrooms"])
        dateListed.append(r["dateListed"])
        seoUrl.append(r["seoUrl"])
    #convert list to data frame
   # df = pd.DataFrame('Salemode': salemode, 'priceDetails': priceDetails, 'address':address, 'streetNumber':streetNumber, 'street':street, 'suburb':suburb, 'postcode':postcode, 'bathrooms':bathrooms, 'dateListed':dateListed, 'seoUrl':seoUrl)
    col = []
    df = pd.DataFrame()
    print(df)
    timeD=time.strftime("%Y-%m-%d-%H%S",time.localtime())
    df.to_excel(timeD+'.csv', index=False)
get_property()