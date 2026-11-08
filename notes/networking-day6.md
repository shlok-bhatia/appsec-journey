
# Networking Day 6 - DNS, IP, Ports and Local Network

## 1. IP Address and CIDR

Command:
```bash
ip addr
```

- Shows network interfaces and IP addresses.
- IP address identifies a device on a network.
- CIDR represents the network prefix.
- /24 means 24 bits are reserved for the network portion.

My IP:
My CIDR:

## 2. Default Gateway

Command:
```bash
ip route
```

- Shows routing information.
- Default gateway forwards traffic to other networks.
- Usually the router's IP address.

My Gateway:

## 3. Neighbor Discovery

Command:
```bash
ip neigh
```

- Displays known neighboring devices.
- Shows IP and MAC addresses.
- Uses the ARP/neighbor cache.

Devices found:

## 4. DNS Lookup

Command:
```bash
dig google.com
```

- Resolves domain names into IP addresses.
- A record represents an IPv4 address.

Command:
```bash
dig +trace google.com
```

- Shows the DNS resolution chain.
- Root -> TLD -> Authoritative DNS.

## 5. WHOIS

Command:
```bash
whois google.com
```

- Displays domain registration information.
- Shows registrar, dates and name servers.

## 6. Listening Ports

Command:
```bash
ss -tulpn
```

- Shows listening TCP and UDP sockets.
- Helps identify services running on a machine.

## 7. Important Ports

| Port | Service |
|------|---------|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 8080 | Alternative HTTP |

## 8. What I Learned

- How to find my IP address.
- How CIDR notation works.
- How to identify my default gateway.
- How DNS resolution works.
- How to inspect nearby devices.
- How to identify listening ports.



## 9. DNS Trace Analysis

Command:
```bash
dig +trace google.com
```

### What I learned

- DNS resolution starts from the Root DNS servers.
- Root servers direct queries to TLD servers.
- TLD servers direct queries to authoritative DNS servers.
- Authoritative DNS servers provide the actual DNS records.

### DNS Resolution Flow

Root DNS (.)
      |
      v
TLD DNS (.com)
      |
      v
Authoritative DNS (google.com)
      |
      v
Final IP Address

### Important DNS Records

- NS: Name Server
- A: IPv4 Address
- AAAA: IPv6 Address
- DS: Delegation Signer
- RRSIG: DNSSEC Signature
- NSEC3: Authenticated proof of non-existence

### My Observation

The command successfully resolved google.com
and returned the IPv4 address:

142.250.193.14

Some IPv6 DNS queries timed out, but the
overall DNS resolution completed successfully.
