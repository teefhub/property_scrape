import requests
import json
import

# set up
client_id = 'client_efea88970efe3e446d19fe9348b1eb51'
client_secret = 'secret_059802205992820c83479e71c92de02a'
scopes = ['api_properties_read']
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_endpoint = 'https://api.domain.com.au/v1/listings/residential/_search'

def get_data():
    response = requests.post(auth_url, data = {
                        'listingType':"sale",
                        'propertyTypes':["House","NewApartments"],
                        'locations':
                        'Content-Type':'text/json'
                        })

  "propertyTypes":[
    "House",
    "NewApartments"
  ],
  "minBedrooms":3,
  "minBathrooms":2,
  "minCarspaces":1,
  "locations":[
    {
      "state":"NSW",
      "region":"",
      "area":"",
      "suburb":"Newtown",
      "postCode":"",
      "includeSurroundingSuburbs":false
    }
  ]
}