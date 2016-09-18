import requests
import simplejson
data = {'id':   '1'}
data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}
r = requests.post("http://localhost:8080/api/songs", data=payload)
print(r.json)
