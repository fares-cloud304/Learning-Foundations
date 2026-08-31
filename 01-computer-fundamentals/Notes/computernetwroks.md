# Lesson 8 — Computer Networks: How Computers Talk

## 1. What Is a Network?

A network is **two or more computers connected to share data**.

The simplest network is two computers connected by a cable.

The **internet** is the largest network, connecting billions of computers globally.

### Network Scales

* **LAN (Local Area Network)** — a small local network, such as your home Wi-Fi.
* **WAN (Wide Area Network)** — connects networks across cities or countries.
* **Internet** — the global network connecting computers worldwide.

---

## 2. IP Addresses

Every device on a network has an **IP address** — a unique identifier, similar to a phone number.

Example IPv4 address:

```text
192.168.1.100
```

IPv4 addresses are running out, so **IPv6** was created.

Example IPv6 address:

```text
2001:0db8:85a3:8a2e:0370:7334
```

---

## 3. Packets

When Computer A wants to send data to Computer B, it breaks the data into **packets** (small chunks).

The packets are labelled with Computer B's IP address and sent through the network.

---

## 4. Routers

A **router** is a specialized computer that directs packets toward their destination.

It helps determine where packets should go when traveling between different networks.

---

## 5. Ports

A **port** identifies a specific service running on a computer.

Think of the IP address as identifying the **computer**, while the port identifies the **service** on that computer.

For example:

```text
192.168.1.100:443
```

This means:

* `192.168.1.100` → the computer
* `443` → the service using port 443

### Common Ports

| Port | Protocol / Service | Use                   |
| ---: | ------------------ | --------------------- |
|   80 | HTTP               | Web traffic           |
|  443 | HTTPS              | Encrypted web traffic |
|   22 | SSH                | Secure remote access  |
|   53 | DNS                | Domain Name System    |

---

## 6. Protocols

Protocols are the rules computers use to communicate.

### HTTP

**HTTP (Hypertext Transfer Protocol)** is used for web pages.

### HTTPS

**HTTPS** is HTTP with encryption using TLS/SSL.

### SSH

**SSH (Secure Shell)** is used for encrypted remote access to computers.

### DNS

**DNS (Domain Name System)** translates human-readable names such as:

```text
google.com
```

into IP addresses such as:

```text
142.250.x.x
```

### TCP

**TCP (Transmission Control Protocol)** provides reliable delivery.

If a packet is lost, TCP can arrange for it to be sent again.

### UDP

**UDP (User Datagram Protocol)** is faster but does not guarantee delivery.

It can be useful for things such as video streaming and gaming.

---

## 7. Firewalls

Firewalls are lists of rules that control network traffic.

For example:

```text
Allow traffic on port 443.
Block everything else.
```

A firewall can therefore control which network connections are allowed or blocked.

---

## 8. Basic Computer-to-Computer Communication

The basic flow is:

```text
Computer A
    ↓
Data is broken into packets
    ↓
Packets are given Computer B's IP address
    ↓
Packets travel through the network
    ↓
Routers direct the packets
    ↓
Computer B receives the packets
```

---

## Key Takeaways

* A **network** connects computers so they can communicate and share data.
* An **IP address** identifies a device on a network.
* **Packets** are small chunks of data sent across a network.
* **Routers** direct packets toward their destinations.
* **Ports** identify specific services running on a computer.
* **HTTP** is used for web traffic.
* **HTTPS** is encrypted web traffic.
* **SSH** provides encrypted remote access.
* **DNS** translates domain names into IP addresses.
* **TCP** provides reliable delivery.
* **UDP** is faster but does not guarantee delivery.
* **Firewalls** control which network traffic is allowed or blocked.
* **LAN**, **WAN**, and the **internet** describe networks at different scales.
* **IPv6** was created because IPv4 addresses are running out.
