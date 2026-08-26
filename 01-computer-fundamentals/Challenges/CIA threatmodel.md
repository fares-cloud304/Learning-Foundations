# Lesson 9 — CIA Triad — Challenge 3

## Mobile Banking App Threat Model

### Objective

Create a basic threat model for a mobile banking application by identifying **5 major threats** and determining which components of the **CIA Triad** each threat could affect.

For this exercise, the banking application is treated as a system containing sensitive financial information, user accounts, authentication credentials, and financial transactions.

---

## Threat 1 — Phishing

### Description

An attacker may create a fake banking login page or send a deceptive message designed to trick a user into revealing their banking credentials.

### Potential Impact

If the attacker obtains the user's credentials, they may gain unauthorized access to private banking information.

### CIA Component

**Confidentiality**

### Reason

Private account information and credentials may be exposed to an unauthorized person.

---

## Threat 2 — Account Takeover

### Description

An attacker may gain control of a customer's banking account through stolen credentials or compromised authentication.

### Potential Impact

The attacker could access private account information and potentially perform unauthorized actions.

### CIA Components

**Confidentiality + Integrity**

### Reason

* **Confidentiality:** The attacker can access information they are not authorized to see.
* **Integrity:** The attacker may be able to modify account information or perform unauthorized transactions.

---

## Threat 3 — Unauthorized Transaction

### Description

An attacker who gains access to an account could attempt to create or modify a financial transaction without the legitimate user's authorization.

### Potential Impact

The account's financial information and transaction history could be improperly changed.

### CIA Component

**Integrity**

### Reason

The system's legitimate transaction state has been improperly modified.

---

## Threat 4 — Malware on the User's Device

### Description

Malicious software on a user's phone could potentially monitor sensitive information or interfere with activity performed through the banking application.

### Potential Impact

Sensitive banking information could be exposed, or actions performed by the user could potentially be manipulated.

### CIA Components

**Confidentiality + Integrity**

### Reason

* **Confidentiality:** Sensitive information could be exposed.
* **Integrity:** Banking activity could potentially be altered or manipulated.

---

## Threat 5 — DDoS Attack

### Description

An attacker could overwhelm banking infrastructure with a large amount of network traffic.

### Potential Impact

Legitimate customers may be unable to access the banking application or its services.

### CIA Component

**Availability**

### Reason

The banking service becomes unavailable or significantly degraded for legitimate users.

---

# Threat Summary

| # | Threat                   | CIA Component(s)                | Main Impact                                    |
| - | ------------------------ | ------------------------------- | ---------------------------------------------- |
| 1 | Phishing                 | **Confidentiality**             | Credentials/private information exposed        |
| 2 | Account takeover         | **Confidentiality + Integrity** | Unauthorized access and actions                |
| 3 | Unauthorized transaction | **Integrity**                   | Financial data/transactions improperly changed |
| 4 | Malware on user's device | **Confidentiality + Integrity** | Information exposed or activity manipulated    |
| 5 | DDoS attack              | **Availability**                | Banking service becomes inaccessible           |

---

# Threat Model

```text id="4y7x6e"
                    MOBILE BANKING APP
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
   CONFIDENTIALITY      INTEGRITY       AVAILABILITY
          │                │                │
      Phishing       Unauthorized       DDoS attack
      Malware        transactions
      Account        Account takeover
      takeover
          │                │
          └────────┬───────┘
                   ↓
              Malware
```

## Key Lesson

Threat modeling means asking:

> **What can go wrong, who could cause it, what could they affect, and which security objective is threatened?**

The CIA Triad provides a useful way to classify the impact:

* **Confidentiality** → unauthorized access or disclosure.
* **Integrity** → unauthorized modification or manipulation.
* **Availability** → preventing legitimate users from accessing the service.

### Challenge Result

**5 major threats identified and mapped to the CIA Triad.**

* Confidentiality threats identified: **3**
* Integrity threats identified: **3**
* Availability threats identified: **1**

**Result: Challenge 3 — Complete**
