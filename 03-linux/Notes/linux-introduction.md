Phase 3, Lesson 1: Linux Introduction & File System
Overview
Linux is the undisputed king of the cloud, running over 90% of cloud workloads. For a cloud security engineer, mastering the Linux file system and CLI is non-negotiable. Unlike Windows, Linux uses a single unified tree structure starting from the root directory (/).

1. The Linux Ecosystem (Distros)
Linux is just a "kernel" combined with different tools to create Distributions (Distros).

Ubuntu: Most popular for beginners and AWS cloud.
CentOS/RHEL: Enterprise-focused.
Debian: Stable and minimal.
Alpine: Tiny (5MB) and heavily used in Docker containers.
Note: Commands are mostly the same across distros, but package managers differ (apt vs yum vs apk).
2. Why Linux Dominates the Cloud
Cost: It is free and open-source.
Lightweight: Servers don't need a heavy GUI (Graphics User Interface).
Security: Built-in user permissions, SELinux, and powerful networking tools.
AWS Integration: When launching an EC2 instance, you choose a Linux AMI (Amazon Machine Image). Ubuntu and Amazon Linux are the defaults.
3. The Linux File System Hierarchy
Linux does not use C:\ or D:\. Everything starts at / (root) and branches out like a tree. USB drives and network shares are "mounted" into this single tree.

Key Directories:
Directory	Purpose
/	The root of the entire file system.
/home	Where normal users store their personal files.
/etc	Configuration files (where security settings live).
/var	Variable data (logs, databases).
/var/log	The goldmine for security analysts (system and app logs).
/usr	Installed programs and user utilities.
/bin & /sbin	Essential system command binaries.
/tmp	Temporary files (often cleared on reboot).
/root	The home directory for the root (superuser) account.
4. Cloud Security Implications
/etc/passwd & /etc/shadow: Store user account information and password hashes. A prime target for attackers.
/var/log: The first place you look during an incident response to see what an attacker did.
/etc/ssh/sshd_config: The file you edit to disable password login and secure SSH on a cloud server.
