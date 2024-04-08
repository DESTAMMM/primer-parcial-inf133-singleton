import request
import requests

url = "http://localhost:8000/guess"

response = requests.request(method="GET", url=url)
print(response.text)