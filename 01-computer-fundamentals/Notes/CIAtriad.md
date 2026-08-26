# Lesson 9 — CIA Triad — Challenge 1

## CIA Identification

### Objective

Identify which component of the **CIA Triad** is primarily affected by different cybersecurity incidents.

The CIA Triad consists of:

* **Confidentiality** — preventing unauthorized access to information.
* **Integrity** — preventing unauthorized or improper modification of information.
* **Availability** — ensuring systems and information remain accessible when needed.

---

## Scenarios

### A. Hacker defaces a website

**Answer: Integrity**

The hacker has unauthorizedly modified the website's content.

The website may still be online and accessible, but its information/content has been changed.

**CIA component affected:** `Integrity`

---

### B. DDoS attack takes down a store

**Answer: Availability**

A DDoS attack overwhelms a service with traffic, preventing legitimate users from accessing it.

**CIA component affected:** `Availability`

---

### C. Stolen laptop contains unencrypted patient records

**Answer: Confidentiality**

Unauthorized people can potentially access sensitive patient information because the records are not properly protected.

**CIA component affected:** `Confidentiality`

---

## Final Answers

| Scenario                                       | CIA Component       | Why                                                  |
| ---------------------------------------------- | ------------------- | ---------------------------------------------------- |
| Hacker defaces a website                       | **Integrity**       | Data/content was unauthorizedly changed              |
| DDoS takes down a store                        | **Availability**    | Legitimate users cannot access the service           |
| Stolen laptop with unencrypted patient records | **Confidentiality** | Unauthorized people can access sensitive information |

## Quick Memory Trick

**C — Confidentiality** → *Who can see it?*

**I — Integrity** → *Was it changed?*

**A — Availability** → *Can I access it?*
