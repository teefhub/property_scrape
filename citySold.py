
import requests
import json
import city as api


def get_property_info():
    id = api.city
    response = requests.post(api.auth_url, data = {
                        'client_id':api.client_id,
                        'client_secret':api.client_secret,
                        'grant_type':'client_credentials',
                        'scope':api.scopes,
                        'Content-Type':'text/json'
                        })
    #print(response)
    json_res = response.json()
    access_token=json_res['access_token']
    #print(access_token)
    auth = {'Authorization':'Bearer ' + access_token}

    url = api.url_endpoint

    res1 = requests.get(url, headers=auth)
    #print(res1)
    r = res1.json()
    print(r)
    print(len(r))
    list = []
    for i in range(len(r)):
        streetNumber = r[i]["streetNumber"]
        list.append(streetNumber)
        print(streetNumber)
        
    print("END OF LIST")
get_property_info()