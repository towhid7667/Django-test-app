import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Hello World from Towhid",
    "price": "20.00"
}
r = requests.post(endpoint, json=data)

# print(r.text)
print(r.json())
print(r.status_code)
