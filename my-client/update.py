import requests

endpoint = "http://localhost:8000/api/products/1/update"
data = {
    "title": "Hello Reaz",
    "price": 20.00
}
r = requests.put(endpoint, json=data)

# print(r.text)
print(r.json())
print(r.status_code)
