import requests
import json
client_id = 'client_efea88970efe3e446d19fe9348b1eb51'
client_secret = 'secret_059802205992820c83479e71c92de02a'
auth_url = 'https://auth.domain.com.au/v1/connect/token'
response = requests.post(auth_url, data = {
                        'client_id':client_id,
                        'client_secret':client_secret,
                        'grant_type':'client_credentials',
                        'scope':scopes,
                        'Content-Type':'text/json'
                        })
json_res = response.json()
access_token=json_res['access_token']
auth = {'Authorization':'Bearer ' + access_token}