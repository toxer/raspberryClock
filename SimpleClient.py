import requests
import simplejson
data = {'id':   '1'}
data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}
headers = {'content-type': 'application/json'}
r = requests.post("http://localhost:8080/api/songs",headers=headers, data=data_json)

print(r.json())
