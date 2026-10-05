Lab: Linux Package Managers Comparison
Overview
A package manager is a tool that automates the process of installing, upgrading, configuring, and removing software on a Linux system. Different Linux distributions use different package managers. As a Cloud Security Engineer, you must know which one to use based on the server you are auditing or hardening.

1. apt (Advanced Package Tool)
Distributions: Debian, Ubuntu, WSL (Windows Subsystem for Linux).
Install Command: sudo apt install <package>
Update Command: sudo apt update && sudo apt upgrade
When to use it: This is the most common package manager you will use in the cloud. If you launch an Ubuntu or Debian EC2 instance on AWS, you will use apt to install security tools like nmap, fail2ban, or docker.
2. yum / dnf (Yellowdog Updater, Modified / Dandified YUM)
Distributions: RHEL (Red Hat Enterprise Linux), CentOS, Amazon Linux 2, Fedora.
Install Command: sudo dnf install <package> (or yum install)
Update Command: sudo dnf upgrade
When to use it: If you are working in an enterprise environment, government cloud, or using AWS's default Amazon Linux AMI, you will use dnf or yum. It is heavily used in corporate data centers and enterprise compliance environments.
3. apk (Alpine Package Keeper)
Distributions: Alpine Linux.
Install Command: apk add <package>
Update Command: apk update && apk upgrade
When to use it: You will use apk almost exclusively when working with Docker containers. Because Alpine Linux is only 5MB, it is the industry standard for building minimal, highly-secure Docker images. You use apk to install the absolute minimum dependencies needed for your containerized apps.
Summary Table
Feature	apt	dnf / yum	apk
Distro	Ubuntu / Debian	RHEL / Amazon Linux	Alpine
Target	Cloud VMs, Desktops	Enterprise Cloud VMs	Docker Containers
Security Benefit	Massive repos, well-tested	Enterprise stability, long support	Tiny attack surface
