import requests
import json

# set up
client_id = 'client_efea88970efe3e446d19fe9348b1eb51'
client_secret = 'secret_059802205992820c83479e71c92de02a'
scopes = ['api_addresslocators_read']
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_endpoint = 'https://api.domain.com.au/v1/addressLocators?searchLevel=Address&streetNumber=36&streetName=Longfield&streetType=Street&suburb=Cabramatta&state=NSW'
 # &suburb=Pyrmont&state=NSW&postcode=2009

def get_property_info():
    # post When you send some data on server then use post methods
    response = requests.post(auth_url, data={
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': scopes,
        'Content-Type': 'text/json'
    })
    #print(response)
    json_res = response.json()
    access_token = json_res['access_token']
    #print(access_token)
    auth = {'Authorization': 'Bearer ' + access_token}
    url = url_endpoint
    res1 = requests.get(url, headers=auth)
    r = res1.json()
    print(r[0]["ids"][2])
    print(r[0]["addressComponents"][1])
    # accessing a list of dictionaries
    #for i in range(len(r)):
       # print(r[i]["addressComponents"][1])


        # not needed
        # else:
        # print("No result")


get_property_info()