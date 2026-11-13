
# Burp Suite - Day 10

## 1. Objective
Configure Burp Suite from scratch and understand
how to intercept and modify HTTP/HTTPS traffic.

## 2. Proxy Listener
- Bind Address: 127.0.0.1
- Port: 8080
- Intercept: OFF during normal browsing
- Intercept: ON during testing

## 3. CA Certificate
- Opened http://burp
- Downloaded cacert.der
- Imported certificate into Firefox Authorities
- Enabled trust for identifying websites
- Verified HTTPS inspection without certificate warnings

## 4. FoxyProxy
- Installed FoxyProxy Standard
- Proxy Type: HTTP
- Host: 127.0.0.1
- Port: 8080

## 5. Target Scope
Added authorized testing targets:
- httpbin.org
- portswigger.net (including subdomains)

Enabled in-scope filtering in HTTP History.

## 6. HTTP Interception

### GET Request
Endpoint: https://httpbin.org/get

Modified header:
User-Agent: AI-Security-Day10

Observed modified header in the response.

### POST Request
Endpoint: https://httpbin.org/post

Changed:
GET /get -> POST /post

Added request body:
q=burp&day=10

Observed submitted data in the JSON response.

## 7. Concepts Learned
- Proxy Listener
- Burp CA Certificate
- HTTPS Interception
- FoxyProxy
- Target Scope
- HTTP History
- GET and POST
- Request Header Modification
- Request Body Modification

## 8. Security Notes
- Use Burp only on authorized targets.
- Keep the CA certificate in a dedicated testing browser.
- Disable interception after testing.
- Disable proxy when normal browsing.

## 9. Conclusion
Successfully configured Burp Suite and practiced
intercepting, modifying, forwarding and inspecting
HTTP requests and responses.
