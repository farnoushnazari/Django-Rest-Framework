import requests

endpoint = "http://localhost:8000/api/products/"

response = requests.post(endpoint, json={
    'title': 'well, this is fifth one!',
    })
print(response.json())