
import requests

url = "https://httpbin.org/status/404"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)
    print("Response Body:")
    print(response.text[:200])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
