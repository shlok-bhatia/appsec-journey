
# Day 9 - Python for Cybersecurity

## 1. POST Requests

- POST sends data to a server.
- JSON is commonly used to send structured data.
- Headers provide additional request information.

Example:

```python
import requests

r = requests.post(
    "https://httpbin.org/post",
    json={"user": "admin", "role": "guest"},
    headers={"X-Test": "venice"}
)

print(r.status_code)
print(r.json())
```

## 2. JSON Parsing

- JSON is a format used for exchanging data.
- r.json() converts JSON responses into Python dictionaries.
- Nested dictionary values can be accessed using keys.

Example:

```python
data = r.json()
print(data["args"])
```

## 3. Query Parameters

- params= automatically builds URL query parameters.
- It avoids manually concatenating query strings.

Example:

```python
requests.get(
    "https://httpbin.org/get",
    params={"q": "sql"}
)
```

## 4. Argparse

- argparse accepts command-line arguments.
- It makes scripts reusable for different targets.

Important methods:

```python
argparse.ArgumentParser()
p.add_argument()
p.parse_args()
```

Example:

```bash
python3 scripts/argparse_get.py -u https://example.com
```

## 5. Error Handling

- try contains code that may fail.
- except handles errors.
- timeout prevents requests from waiting indefinitely.

Important exceptions:

```python
requests.exceptions.Timeout
requests.exceptions.ConnectionError
requests.exceptions.RequestException
```

## 6. HTTP Status Codes

- 200: OK
- 301: Permanent redirect
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Internal server error

## 7. Saving Output

Python can save HTTP responses into files.

Example:

```python
with open("out.txt", "w") as f:
    f.write(r.text)
```

- open() opens or creates a file.
- w means write mode.
- write() saves the response.
- with automatically closes the file.

## 8. What I Learned

- Sending POST requests.
- Working with JSON request bodies.
- Using custom HTTP headers.
- Parsing JSON responses.
- Using argparse for command-line input.
- Handling network errors and timeouts.
- Saving HTTP responses to files.

## 9. Cybersecurity Applications

These concepts are useful for:

- API security testing.
- HTTP automation.
- Web reconnaissance.
- Security scanning scripts.
- Collecting and analyzing HTTP responses.
