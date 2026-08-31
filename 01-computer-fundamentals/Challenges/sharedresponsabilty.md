# Cloud Security Practice: Shared Responsibility Analysis

A structured documentation of an AWS cloud architecture challenge focusing on the **AWS Shared Responsibility Model**. This case study demonstrates proficiency in distinguishing between security "of" the cloud (Provider responsibility) and security "in" the cloud (Customer responsibility).

## 📋 Challenge Overview

The objective of this challenge is to correctly attribute infrastructure, configuration, operational, and physical security tasks to either **AWS (the Cloud Provider)** or **The Customer**.

### Scenario Parameters Evaluated:
* Physical data center security
* Amazon S3 bucket access policies
* Amazon EC2 guest operating system patching
* Amazon S3 underlying hardware maintenance

---

## 🛠️ Analysis & Resolution

| Scenario | Component | Responsibility | Technical Context | Status |
| :--- | :--- | :--- | :--- | :---: |
| **A** | Physical Data Center Security | **Provider (AWS)** | AWS controls physical access, facilities, perimeter security, and environmental systems. | `PASSED` ✅ |
| **B** | S3 Bucket Policy | **Customer** | The customer controls resource access permissions, encryption policies, and public access blocks. | `PASSED` ✅ |
| **C** | EC2 OS Patches | **Customer** | For IaaS resources, the guest operating system, firewall software, and application patches are user-managed. | `PASSED` ✅ |
| **D** | S3 Hardware Maintenance | **Provider (AWS)** | AWS manages abstract storage infrastructure, replacing degraded disks and physical servers silently. | `PASSED` ✅ |

### Final Score
```text
Score: 4 / 4 (100% Accuracy)
Status: Perfect Performance
```

---

## 🧠 Architectural Deep Dive: The Core Rule

To build securely on AWS, architectural decisions follow a strict operational boundary line:

```text
    AWS GLOBAL INFRASTRUCTURE
    ├── [PROVIDER]  Physical Data Centers (Cooling, Power, Guards)
    ├── [PROVIDER]  Physical Hardware & Host Servers (Disks, Racks)
    └── [PROVIDER]  Managed Infrastructure (S3/RDS Managed Storage Layers)
    
    YOUR DEPLOYED ARCHITECTURE
    ├── [CUSTOMER]  Data Governance & S3 Bucket Policies
    ├── [CUSTOMER]  EC2 Guest Operating Systems (Updates, Firewalls)
    └── [CUSTOMER]  Application Code & Identity Access Management (IAM)
```

### Key Takeaways
1. **Security OF the Cloud:** AWS protects the global infrastructure that executes all offered cloud services.
2. **Security IN the Cloud:** The customer manages configurations, endpoints, data classification, and logical access permissions.
