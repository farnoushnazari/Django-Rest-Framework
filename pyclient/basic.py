import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title": "Test Product"})
print(response.json())