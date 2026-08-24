# Lesson 8 — Challenge 2: Identify Listening Ports

## Objective

Use Linux networking tools to identify **listening network ports** and determine which services are using them.

---

## Commands Used

### Check TCP listening sockets

```bash
ss -tuln
```

### Check TCP and UDP sockets with process information

```bash
sudo ss -tulpn
```

### Check UDP sockets

```bash
sudo ss -ulpn
```

---

## Results

### TCP

The system had the following TCP listening sockets:

| Local Address    | Port | Protocol | Service      |
| ---------------- | ---: | -------- | ------------ |
| `127.0.0.53%lo`  |   53 | TCP      | DNS resolver |
| `127.0.0.54`     |   53 | TCP      | DNS resolver |
| `10.255.255.254` |   53 | TCP      | DNS service  |

Port **53** is used by DNS.

---

### UDP

The system had the following UDP sockets:

| Local Address    | Port | Protocol | Process           | Purpose                   |
| ---------------- | ---: | -------- | ----------------- | ------------------------- |
| `127.0.0.54`     |   53 | UDP      | `systemd-resolve` | DNS resolution            |
| `127.0.0.53%lo`  |   53 | UDP      | `systemd-resolve` | DNS resolution            |
| `10.255.255.254` |   53 | UDP      | —                 | DNS endpoint              |
| `127.0.0.1`      |  323 | UDP      | `chronyd`         | Time synchronization      |
| `::1`            |  323 | UDP      | `chronyd`         | IPv6 time synchronization |

---

## Understanding the Results

### Port 53 — DNS

DNS normally uses **UDP port 53**, but it can also use **TCP port 53**.

The system showed both:

```text
TCP :53
UDP :53
```

`systemd-resolve` was responsible for some of the local DNS sockets.

---

### Port 323 — Chrony

Port `323` was being used by:

```text
chronyd
```

`chronyd` is a time synchronization service.

The addresses:

```text
127.0.0.1
::1
```

represent **localhost**.

* `127.0.0.1` → IPv4 localhost
* `::1` → IPv6 localhost

Therefore, these sockets are associated with the local system rather than being directly exposed on the local network.

---

## Understanding `LISTEN` vs `UNCONN`

TCP commonly appears as:

```text
LISTEN
```

because TCP services wait for incoming connections.

UDP commonly appears as:

```text
UNCONN
```

because UDP is **connectionless**.

`UNCONN` does **not** mean the service is broken or unavailable.

---

## Key Concepts Learned

* `ss` can inspect network sockets on Linux.
* `sudo ss -tulpn` can show TCP/UDP sockets and associated processes.
* **Port 53** → DNS.
* **Port 323** → chrony/time synchronization.
* `127.0.0.1` and `127.0.0.53` → IPv4 localhost addresses.
* `::1` → IPv6 localhost.
* `10.255.255.254` → private IPv4 address.
* TCP commonly shows `LISTEN`.
* UDP commonly shows `UNCONN` because it is connectionless.
* A port being present does not automatically mean it is publicly accessible; the **listening address, routing, firewall, and network configuration** also matter.

## Practical Security Lesson

Knowing an IP address is not enough to determine whether a service is accessible.

A useful investigation chain is:

```text
IP address
    ↓
Port
    ↓
Protocol
    ↓
Listening service
    ↓
Process
    ↓
Firewall / network exposure
```

This is an important foundation for later **Linux administration, cloud networking, and cloud security**.
