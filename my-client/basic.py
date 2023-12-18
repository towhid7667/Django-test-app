import requests

endpoint = "http://localhost:8000/api/"

r = requests.post(endpoint,json={"title": "Hello World"})

# print(r.text)
print(r.json())
print(r.status_code)
