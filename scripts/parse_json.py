
import requests

url = "https://httpbin.org/get"

try:
    r = requests.get(
        url,
        params={"q": "sql"},
        timeout=(5, 10)
    )

    r.raise_for_status()

    data = r.json()

    print("Status Code:", r.status_code)
    print("Search Query:", data["args"]["q"])
    print("Host:", data["headers"].get("Host"))

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Connection failed!")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

except ValueError:
    print("Invalid JSON response!")

