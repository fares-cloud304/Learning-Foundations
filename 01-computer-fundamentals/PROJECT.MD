# Computer Fundamentals — Phase 1

## Overview

This repository documents my Phase 1 journey into computer science,
Linux, networking, cybersecurity, and cloud computing.

The goal of this phase was to build strong technical foundations
before moving into deeper cloud security engineering.

---

## What I Learned

### 1. Computer Fundamentals

- CPU
- CPU cores
- GHz / clock speed
- RAM
- Storage
- SSD vs HDD
- Motherboard
- How hardware components work together
- Why insufficient RAM can affect system performance

### 2. Data Representation

- Binary
- Bits and bytes
- Decimal
- Hexadecimal
- Why computers use binary
- Hexadecimal representation
- SHA-256 hashing
- File integrity
- Magic bytes
- Hex dumps

### 3. Operating Systems

- Operating system fundamentals
- Kernel
- User space
- System calls
- Application → kernel → hardware relationship
- Privilege separation
- `strace`
- `strace -c`

### 4. Linux Fundamentals

- Files and directories
- Inodes
- File metadata
- Hard links
- Symbolic links
- Linux filesystem concepts
- Basic Linux commands

Commands practiced:

```bash
ls -la
cd
cp
mv
rm
touch
mkdir
find
file
hexdump
5. File Investigation

I learned how to investigate files instead of trusting
their filenames or extensions.

Tools practiced:

file
hexdump
exiftool
steghide

Concepts:

Magic bytes
File signatures
Metadata
EXIF data
GPS metadata
Steganography
Hidden data

Example investigation workflow:

Unknown file
    ↓
file
    ↓
Check actual file type
    ↓
hexdump
    ↓
Inspect raw bytes if necessary
    ↓
exiftool
    ↓
Inspect metadata
    ↓
steghide
    ↓
Check for hidden data
6. System Investigation
CPU usage
RAM usage
Storage usage
Processes
System calls
Investigating unusual system behavior
Using strace to understand application behavior
7. Storage & Cloud Fundamentals
RAM vs persistent storage
SSD vs HDD
Block storage
Object storage
File storage
Amazon EBS
Amazon S3
Amazon EFS

Basic distinction:

EBS → Block storage
S3  → Object storage
EFS → File storage
8. Networking
What a computer network is
Private IP addresses
Public IP addresses
IPv4
IPv6
DNS
TCP
UDP
Ports
Routers
NAT
Localhost
Listening services
Network traffic flow

Important concepts:

Private IP
    ↓
Router
    ↓
NAT
    ↓
Public IP
    ↓
Internet
    ↓
Destination server

Common ports studied:

22   → SSH
53   → DNS
80   → HTTP
443  → HTTPS

Command practiced:

ss -tuln
9. Cybersecurity Fundamentals
CIA Triad
Confidentiality

Prevent unauthorized access to information.

Integrity

Prevent or detect unauthorized modification of information.

Availability

Keep systems and information accessible to legitimate users.

Examples:

Data exposed        → Confidentiality
Data modified       → Integrity
Service unavailable → Availability
Threat Modeling

I learned to identify threats and determine which CIA component
they affect.

Example:

DDoS
 ↓
Service overwhelmed
 ↓
Users cannot access it
 ↓
Availability
AWS Security Services
Confidentiality
AWS KMS
AWS CloudHSM
AWS Certificate Manager
Integrity
Amazon QLDB
AWS CloudTrail
Amazon S3
Availability
AWS Shield
Amazon Route 53
AWS Auto Scaling
10. Cloud Computing
What cloud computing is
Cloud service models
IaaS
PaaS
SaaS
Cloud vs physical infrastructure
Cloud cost concepts
Break-even analysis
Shared responsibility model

Examples:

IaaS
├── AWS EC2
└── Azure Virtual Machines

PaaS
└── Google App Engine

SaaS
├── Gmail
└── Microsoft 365
Shared Responsibility

I learned that cloud security is divided between the provider
and the customer.

Examples:

Physical data center security → Provider
S3 bucket policy              → Customer
EC2 guest OS patches          → Customer
S3 hardware maintenance      → Provider
Skills Demonstrated

During this phase I practiced:

Linux command-line usage
Basic system investigation
File investigation
Understanding system calls
Networking fundamentals
Understanding IP addressing
Understanding ports and protocols
Basic cybersecurity analysis
Threat modeling
AWS fundamentals
Cloud service model classification
Cloud cost comparison
Shared responsibility analysis