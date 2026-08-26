# Lesson 9 — CIA Triad — Challenge 2

## AWS Services That Support the CIA Triad

### Objective

Identify **3 AWS services for each component of the CIA Triad** and explain how each service helps protect that security objective.

The CIA Triad consists of:

* **Confidentiality** — preventing unauthorized access to information.
* **Integrity** — preventing unauthorized or improper modification of information.
* **Availability** — keeping systems and information accessible when needed.

---

# 1. Confidentiality

## AWS Key Management Service (KMS)

**What it does:**

AWS KMS generates, controls, and manages cryptographic keys used to encrypt data across AWS services.

**How it supports confidentiality:**

Encryption helps prevent unauthorized people from reading protected data without access to the required cryptographic key.

**CIA component:** Confidentiality

---

## AWS CloudHSM

**What it does:**

AWS CloudHSM provides dedicated hardware-based cryptographic key storage.

**How it supports confidentiality:**

It protects cryptographic keys using dedicated hardware, helping prevent unauthorized access to the keys used to protect sensitive data.

**CIA component:** Confidentiality

---

## AWS Certificate Manager (ACM)

**What it does:**

AWS Certificate Manager provisions, manages, and deploys public and private SSL/TLS certificates.

**How it supports confidentiality:**

TLS can encrypt network traffic between systems, preventing unauthorized parties from reading data while it is being transmitted.

**CIA component:** Confidentiality

> **Important distinction:** ACM manages the certificates. TLS is what provides the encryption for the network traffic.

---

# 2. Integrity

## Amazon QLDB

**What it does:**

Amazon QLDB provides a transparent, immutable, and cryptographically verifiable transaction log that records data changes.

**How it supports integrity:**

The transaction history can be verified, making unauthorized modification of the recorded history detectable.

**CIA component:** Integrity

---

## AWS CloudTrail

**What it does:**

AWS CloudTrail records API activity across AWS infrastructure.

**How it supports integrity:**

CloudTrail Log File Integrity Validation uses cryptographic techniques to help detect whether log files were modified after they were created.

**CIA component:** Integrity

---

## Amazon S3

**What it does:**

Amazon S3 is AWS object storage.

**How it supports integrity:**

S3 provides features such as:

* **S3 Object Lock** — can prevent objects from being deleted or overwritten during a retention period.
* **Checksums** — can help detect data corruption.

These features help ensure stored data remains accurate and protected from unwanted modification.

**CIA component:** Integrity

---

# 3. Availability

## AWS Shield

**What it does:**

AWS Shield helps protect applications against Distributed Denial of Service (DDoS) attacks.

**How it supports availability:**

DDoS attacks can overwhelm services and prevent legitimate users from accessing them. Shield helps mitigate these attacks and keep applications available.

**CIA component:** Availability

---

## Amazon Route 53

**What it does:**

Amazon Route 53 provides highly available DNS and routing capabilities.

**How it supports availability:**

Health checks and routing capabilities can help direct users away from unhealthy endpoints toward healthy ones.

**CIA component:** Availability

---

## AWS Auto Scaling

**What it does:**

AWS Auto Scaling automatically adjusts cloud capacity based on application demand.

**How it supports availability:**

When traffic increases, additional capacity can be added to help applications continue operating without becoming unavailable or severely degraded.

**CIA component:** Availability

---

# Final CIA Mapping

| CIA Component       | AWS Services                                   |
| ------------------- | ---------------------------------------------- |
| **Confidentiality** | AWS KMS, AWS CloudHSM, AWS Certificate Manager |
| **Integrity**       | Amazon QLDB, AWS CloudTrail, Amazon S3         |
| **Availability**    | AWS Shield, Amazon Route 53, AWS Auto Scaling  |

---

# Key Concept

The important lesson is not simply memorizing nine AWS services.

The important relationship is:

**Security objective → problem/threat → control/service**

### Example

```text
DDoS attack
     ↓
Service becomes unavailable
     ↓
Availability is affected
     ↓
AWS Shield helps mitigate the attack
```

Another example:

```text
Unauthorized modification
     ↓
Data cannot be trusted
     ↓
Integrity is affected
     ↓
QLDB / CloudTrail / S3 features can help detect or prevent changes
```

And:

```text
Unauthorized access
     ↓
Sensitive data can be read
     ↓
Confidentiality is affected
     ↓
Encryption + key management help protect the data
```

## Challenge Result

**9 AWS services identified and mapped to the CIA Triad.**

* Confidentiality: **3/3**
* Integrity: **3/3**
* Availability: **3/3**

**Result: 9/9 — Complete**
