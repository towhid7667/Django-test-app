import requests

endpoint = "http://localhost:8000/api/"

r = requests.get(endpoint,params={"abc" : 123}, json={"query": "Hello World"})

# print(r.text)
print(r.json())
print(r.status_code)
