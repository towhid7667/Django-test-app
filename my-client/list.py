import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("Give your User Name?")
password = getpass("Give your password?")


auth_response = requests.post(endpoint, json={'username': username, 'password': password })

# print(r.text)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    r = requests.get(endpoint, headers=headers)

    # print(r.text)
    print(r.json())
    print(r.status_code)
