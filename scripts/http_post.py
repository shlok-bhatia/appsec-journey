
import requests

url = "https://httpbin.org/post"

try:
    r = requests.post(
        url,
        json={"user": "admin", "role": "guest"},
        headers={"X-Test": "venice"},
        timeout=(5, 10)
    )

    print("Status Code:", r.status_code)
    print("Response JSON:", r.json()["json"])
    print("Response Headers:", r.json()["headers"])

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Could not connect to the server!")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
