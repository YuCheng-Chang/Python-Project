import requests
import json
r = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY")
NASA = r.json()
NASA.update(datatype="dictionary")
print(type(NASA))
with open("NASA.json","w") as f:
    json.dump(NASA,f)
with open("NASA.json","r") as f:
    data=json.load(f)
print(data['datatype'])