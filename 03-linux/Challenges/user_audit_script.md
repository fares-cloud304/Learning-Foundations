Lab: User Audit Script
Overview
During a security audit, you need to quickly identify the most dangerous accounts on a Linux server: those that have a valid shell (meaning they can log in) AND have sudo (administrator) privileges.

The Commands
1. Find users with a login shell
Users are stored in /etc/passwd. We filter out system accounts (which use /nologin or /false) to find actual humans/apps that can log in.

grep -v -E "(nologin|false)$" /etc/passwd | cut -d: -f1
(Explanation: grep -v excludes lines. -E "(nologin|false)$" matches system accounts. cut -d: -f1 splits the line by the : colon and grabs the first field: the username).

2. Find users with sudo access
We check the /etc/group file for the sudo group.

bash

grep '^sudo' /etc/group | cut -d: -f4
(Explanation: Finds the sudo group, then extracts the 4th field, which lists the users in that group).

Why this matters in Cloud Security
Attackers try to create backdoor accounts with sudo privileges. If you run these commands and see a user you don't recognize, you have found a backdoor account created by an intruder.