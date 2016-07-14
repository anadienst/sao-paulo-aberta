import requests

req = None
url = "http://127.0.0.1:4569/oi"

headers = {
    'cache-control': "no-cache",
    'postman-token': "51d80d18-fdba-6053-f3f6-8eef9fe9c81a"
}

response = requests.request("POST", url, headers=headers, json={"key": "value"})

print(response.text)