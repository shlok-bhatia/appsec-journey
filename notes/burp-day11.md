# Day 11 – Burp Suite Repeater Mastery

## 1. Introduction to Repeater

- Repeater is a Burp Suite tool used to manually modify and resend HTTP requests.
- It helps understand how servers respond to different requests.
- Requests can be sent multiple times without using the browser again.

## 2. HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update/replace data |
| DELETE | Delete data |
| PATCH | Partially update data |

### What I learned
- Different endpoints support different HTTP methods.
- Unsupported methods can return 405 Method Not Allowed.
- `/anything` on httpbin can be used to test different methods.

## 3. Content-Type

- Content-Type tells the server how to interpret request data.
- `application/x-www-form-urlencoded` is used for form data.
- `application/json` is used for JSON data.
- The same endpoint can process different content types differently.

## 4. URL Parameters

Example:
```http
GET /get?a=1&b=2 HTTP/1.1
Host: httpbin.org
```

- URL parameters send additional data to the server.
- Parameters can be added, removed or modified.
- Duplicate parameters can produce different server-side parsing behavior.

## 5. HTTP Headers and Cookies

- Headers provide additional information about HTTP requests.
- Custom headers can be added using Repeater.
- `Set-Cookie` is sent by the server.
- `Cookie` is sent by the client.
- Cookies can maintain session-related information.

## 6. Response Comparison

- Burp Repeater allows comparison of different responses.
- Helps identify changes in status codes, headers and response bodies.
- Useful for understanding application behavior.

## 7. Tools Used

- Burp Suite Community Edition
- Proxy
- HTTP History
- Repeater
- httpbin.org

## 8. Key Learnings

- Learned to modify HTTP requests manually.
- Understood HTTP methods.
- Explored Content-Type and request-body parsing.
- Practiced modifying URL parameters.
- Understood HTTP headers and cookies.
- Learned to compare HTTP responses.

## Conclusion

Today I learned how Burp Suite Repeater works and how modifying HTTP requests affects server responses. These concepts are important for web application security testing.
