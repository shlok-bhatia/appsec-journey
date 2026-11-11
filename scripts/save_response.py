
import requests

url = "https://httpbin.org/get"

try:
    r = requests.get(url, timeout=10)

    print("Status Code:", r.status_code)

    with open("out.txt", "w") as f:
        f.write(r.text)

    print("Response saved successfully!")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
