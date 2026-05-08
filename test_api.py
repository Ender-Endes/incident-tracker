import requests

data = {
    "reason": "test hatası",
    "date": "2026-05-08",
    "affected": "sistem",
    "root_cause": "bilinmiyor"
}

response = requests.post("http://127.0.0.1:5000/incidents", json=data)
print(response.json())