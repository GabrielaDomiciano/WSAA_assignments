# Gabriela Domiciano Avellar

# This code sends a request to get data in JSON format. Then, it saves the response to a file called cso.json.

import requests

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'
response = requests.get(url)

with open('cso.json', 'wb') as f:
    f.write(response.content)



# Reference:
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en
# https://realpython.com/python-requests/
