import requests

endpoint = "http://localhost:8000/api/products/4/"

response = requests.get(endpoint)
print(response.json())