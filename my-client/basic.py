import requests

endpoint = "https://httpbin.org/anything"

r = requests.get(endpoint, json={"query": "Hello World"})

print(r.json())
print(r.status_code)
