import requests
import time
import json 

url = "https://api.prodia.com/v1/sd/generate"

payload = { "prompt": "spongebob cooking krabbie patties" }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-Prodia-Key": "8805b5b8-dab9-433e-b423-e74253cbc88b"
}
headers2 = {
    "accept": "application/json",
    "X-Prodia-Key": "8805b5b8-dab9-433e-b423-e74253cbc88b"
}


response = requests.post(url, json=payload, headers=headers)
response_string = response.text
response_dict = json.loads(response_string)
job_id = response_dict["job"]

response = requests.get("https://api.prodia.com/v1/job/" + job_id, headers=headers2)
response_string = response.text
response_dict = json.loads(response_string)
status = response_dict["status"]
while status != 'succeeded':
    time.sleep(1)
    response = requests.get("https://api.prodia.com/v1/job/" + job_id, headers=headers2)
    response_string = response.text
    response_dict = json.loads(response_string)
    status = response_dict["status"]

response_string = response.text
response_dict = json.loads(response_string)
    
print(response_dict["imageUrl"])