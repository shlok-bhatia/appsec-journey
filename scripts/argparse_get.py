

import argparse
import requests

p = argparse.ArgumentParser(
    description="Simple HTTP GET client"
)

p.add_argument(
    "-u",
    "--url",
    required=True,
    help="Target URL"
)

a = p.parse_args()

try:
    r = requests.get(a.url, timeout=5)

    print("Status Code:", r.status_code)
    print("Response Length:", len(r.text))

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to server")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
