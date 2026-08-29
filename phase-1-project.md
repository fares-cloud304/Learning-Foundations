# Phase 1 Project: Cloud System Investigation

## Purpose

This project uses only the concepts and terminal commands from CloudPath AI Phase 1 Lessons 1–10. It investigates a computer system and compares it with a cloud virtual machine. It does not use Python, Docker, Kubernetes, Terraform, or later-phase technologies.

## Main question

> Is this system healthy, correctly organized, reachable over a network, and protected against basic security problems?

## Project deliverables

Complete these reports in this repository or in the same project folder:

| Report | Purpose |
|---|---|
| `system-report.md` | Hardware, boot process, operating system, and kernel observations |
| `filesystem-report.md` | File systems, inodes, storage usage, and file metadata |
| `network-report.md` | IP addresses, DNS, connectivity, and listening ports |
| `security-report.md` | Findings classified by confidentiality, integrity, and availability |
| `cloud-comparison.md` | Local computer compared with an AWS EC2 virtual machine |

Use an `evidence/` folder for sanitized screenshots or command output. Never upload passwords, access keys, private information, or sensitive logs.

## Lesson mapping

### Lesson 1: How a Computer Works
Explain BIOS/UEFI, POST, the bootloader, CPU, RAM, and storage. Investigate boot information with `dmesg` and `journalctl -b`.

### Lesson 2: CPU, RAM, and Storage
Record CPU details with `lscpu`, memory with `free -h`, disk usage with `df -h`, and live resource usage with `top`.

### Lesson 3: Binary, Hexadecimal, and Data Representation
Convert 42 to binary and 255 to hexadecimal. Hash text with `echo -n "text" | sha256sum`. Inspect a small file with `xxd` or `hexdump -C`.

### Lesson 4: Operating Systems
Record the OS with `cat /etc/os-release` and the kernel with `uname -r`. Explain the kernel, user space, and system calls.

### Lesson 5: File Systems
Use `df -T`, `df -i`, `ls -i`, and `stat` to investigate file systems, inodes, and file metadata. Explain local file systems versus S3 object storage.

### Lesson 6: The Terminal and Command Line
Demonstrate `pwd`, `ls -la`, `cd`, `mkdir`, `cp`, `mv`, `head`, and `find`. Explain what each command does.

### Lesson 7: Digital Media and Metadata
Explain file extensions, magic bytes, metadata, and steganography. Use `file` on safe sample files and explain why changing an extension does not change the real file type.

### Lesson 8: Computer Networks
Record network information with `ip addr show`, test reachability with `ping`, explain DNS, and inspect listening ports with `ss -tlnp`.

### Lesson 9: Security Fundamentals
Classify findings using the CIA Triad. Discuss confidentiality, integrity, and availability risks such as exposed information, changed files, full disks, or unavailable services.

### Lesson 10: Cloud Computing
Compare the local system with AWS EC2. Explain IaaS, virtual machines, shared responsibility, and why OS patches and firewall configuration are the customer’s responsibility on EC2.

## Investigation questions

1. What hardware and operating system does the system use?
2. What happened during the most recent boot?
3. How much CPU, memory, and storage are available?
4. Which file systems are mounted, and how much space do they use?
5. What file metadata and inode information can be observed?
6. What IP address does the system use?
7. Which ports are listening for network connections?
8. Can the system reach another computer on the network?
9. What confidentiality, integrity, or availability risks exist?
10. How would the same investigation apply to an AWS EC2 virtual machine?

## Completion checklist

- [ ] Run the required commands safely.
- [ ] Record observations in your own words.
- [ ] Remove private information from evidence.
- [ ] Complete the five reports.
- [ ] Add sanitized evidence.
- [ ] Add a simple local-computer-to-cloud comparison diagram.
- [ ] Write one paragraph about what you learned from each Lesson 1–10.

## What I learned

Complete this section after the investigation with one short paragraph for each lesson explaining what you learned and how it relates to cloud engineering.
