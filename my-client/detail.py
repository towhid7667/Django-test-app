import requests

endpoint = "http://localhost:8000/api/products/1/"

r = requests.get(endpoint)

# print(r.text)
print(r.json())
print(r.status_code)
