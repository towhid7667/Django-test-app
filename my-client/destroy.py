import requests

product_id = input("What is the id? \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid")
if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

    r = requests.delete(endpoint)

    # print(r.text)
    print(r.status_code, r.status_code == 204)
