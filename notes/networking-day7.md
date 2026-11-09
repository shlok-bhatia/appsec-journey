
# Networking Day 7 - Wireshark and Packet Analysis

## 1. Objective

Learn packet capture, TCP handshake, HTTP traffic
analysis and credential exposure.

## 2. Start Local HTTP Server

Command:
```bash
cd /tmp
python3 -m http.server 8000
```

- Starts a local HTTP server.
- Listens on port 8000.
- localhost refers to 127.0.0.1.

## 3. Start Wireshark

Command:
```bash
sudo wireshark
```

- Opens Wireshark.
- Select lo (loopback) interface.
- Captures local machine traffic.

## 4. Generate HTTP Traffic

Command:
```bash
curl -v http://localhost:8000
```

- Sends an HTTP request.
- Server returns an HTTP response.
- Traffic can be inspected in Wireshark.

## 5. TCP Three-Way Handshake

Three steps:

1. SYN - Client requests connection.
2. SYN-ACK - Server acknowledges request.
3. ACK - Client confirms connection.

This establishes a TCP connection.

## 6. Wireshark Display Filter

```text
tcp.port == 8000
```

- Filters packets using TCP port 8000.

Follow TCP Stream:
Right-click packet -> Follow -> TCP Stream.

## 7. HTTP Basic Authentication

Command:
```bash
curl -v -u admin:secret123 http://localhost:8000
```

- Sends HTTP Basic Authentication credentials.
- Authorization header contains Base64 encoded credentials.
- Credentials are not encrypted by Base64.

Example:
```text
YWRtaW46c2VjcmV0MTIz
```

Decode:
```bash
echo 'YWRtaW46c2VjcmV0MTIz' | base64 -d
```

Output:
```text
admin:secret123
```

## 8. HTTP vs HTTPS

- HTTP sends application data without TLS encryption.
- HTTPS protects data in transit using TLS.
- HTTPS is important for protecting login credentials.

## 9. DNS Packet Capture

Command:
```bash
dig google.com
```

Wireshark filter:
```text
dns
```

- Captures DNS queries and responses.
- Shows domain names and DNS records.

## 10. What I Learned

- How to start a local HTTP server.
- How to capture network traffic.
- How to identify TCP SYN, SYN-ACK and ACK.
- How to inspect HTTP requests.
- How Basic Authentication works.
- Why Base64 is not encryption.
- Why HTTPS is important.
