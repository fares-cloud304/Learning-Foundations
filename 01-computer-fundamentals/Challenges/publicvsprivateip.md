# Lesson 8 — Challenge 1: Public vs Private IP Addresses

## Public IP Address

A **public IP address** is a globally routable IP address used to communicate across the public internet.

A public IP can be assigned to:

* A home or office router
* A directly internet-connected device
* A cloud server or other internet-facing infrastructure

A public IP is generally visible to systems communicating with you over the internet, although **firewalls and other security controls can prevent incoming connections**.

### Example

A home router might have:

```text
Public IP: 85.123.45.67
```

The router uses this public-facing address when communicating with the wider internet.

---

## Private IP Address

A **private IP address** is an IP address used inside an internal network.

Private IP addresses are commonly used for:

* 🏠 Home networks
* 🏢 Company and school networks
* ☁️ Internal cloud/data-center networks

Private IP addresses are **not globally routable on the public internet**.

Different networks can reuse the same private IP address.

For example:

```text
Network A → 192.168.1.100
Network B → 192.168.1.100
```

This is possible because the two addresses belong to different private networks.

---

## Private IPv4 Ranges

The standard private IPv4 ranges are:

| Range                             | Common use                   |
| --------------------------------- | ---------------------------- |
| `10.0.0.0` → `10.255.255.255`     | Large internal networks      |
| `172.16.0.0` → `172.31.255.255`   | Internal/enterprise networks |
| `192.168.0.0` → `192.168.255.255` | Common in home networks      |

### Important

My Ubuntu/WSL environment previously showed:

```text
172.18.15.4
```

This is a **private IP address** because it falls inside:

```text
172.16.0.0 → 172.31.255.255
```

It is therefore not my home's public internet address.

---

## Private IP + Public IP Together

A typical home network can look like:

```text
                    INTERNET
                       ↕
                  Public IP
                  85.123.45.67
                       ↕
                    ROUTER
                       ↕
                Private Network
             ┌─────────┼─────────┐
             ↓         ↓         ↓
            PC       Phone       TV
       192.168.1.100  .101      .102
```

The **private IPs** are used inside the local network.

The **public IP** represents the network to the wider internet.

---

## NAT — Network Address Translation

Home routers commonly use **NAT (Network Address Translation)**.

NAT allows multiple devices with private IP addresses to communicate through a shared public IP address.

For example:

```text
PC
192.168.1.100
      ↓
   Router
      ↓
Public IP
85.123.45.67
      ↓
   Internet
```

When the response comes back, the router keeps track of the connection and sends the appropriate traffic back to the correct internal device.

```text
Internet
    ↓
Public IP
    ↓
Router
    ↓
192.168.1.100
    ↓
PC
```

---

## Key Differences

| Public IP                                    | Private IP                                                          |
| -------------------------------------------- | ------------------------------------------------------------------- |
| Globally routable                            | Used inside private networks                                        |
| Used across the internet                     | Used inside LANs/internal networks                                  |
| Usually assigned by an ISP or cloud provider | Usually assigned by a router, DHCP server, or network administrator |
| Must be globally unique                      | Can be reused in different networks                                 |
| Example: `85.123.45.67`                      | Example: `192.168.1.100`                                            |

---

## Key Takeaways

* **Public IP = globally routable address used for internet communication.**
* **Private IP = internal address used within a local/private network.**
* The three private IPv4 ranges are:

  * `10.0.0.0/8`
  * `172.16.0.0/12`
  * `192.168.0.0/16`
* Multiple devices can share the same private IP across different networks.
* A home router commonly connects the private network to the public internet.
* **NAT** translates/tracks traffic between private addresses and a public-facing address.
* A public IP being globally routable does **not** mean the device is automatically accessible; firewalls and other security controls can block traffic.
