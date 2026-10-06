Lab: File Finder (Incident Response)
Objective
Find all files modified in the last 24 hours in /etc.

The Command
sudo find /etc -type f -mtime -1
(Explanation: find /etc searches the etc directory. -type f looks only for files. -mtime -1 filters for files modified in less than 1 day.)

Why is this useful in Cloud Security?
The /etc directory contains all system configurations, including passwd, shadow, and sshd_config.

If an attacker breaches your server, the first thing they usually do is modify configuration files to create a backdoor, escalate their privileges, or disable the firewall.

During an Incident Response (IR) investigation, running this command immediately tells you exactly which configurations the attacker tampered with in the last 24 hours. It is a digital footprint tracker.