Phase 3, Lesson 3: Users, Groups & Permissions
Overview
Linux is a multi-user operating system, meaning multiple people (and applications) can use the same system simultaneously with separate accounts. Managing who can access what is the absolute foundation of Linux security.

1. Users and Groups
Users: Every user has a unique ID (uid), a home directory (/home/username), and belongs to one or more groups.
Root User: The root user (uid 0) has unlimited power. It can do anything on the system.
User Databases:
/etc/passwd: Stores user info (username, uid, home dir, shell).
/etc/shadow: Stores password hashes. Must be readable ONLY by root.
/etc/group: Stores group membership information.
Service Accounts: In cloud security, applications (like web servers) run as dedicated service accounts with minimal permissions. Regular user SSH access is restricted, and permissions are managed via groups.
2. File Permissions (rwx)
Every file/directory has permissions for three categories:

Owner: The user who owns the file.
Group: A specific group of users.
Others: Everyone else on the system.
Each category has three permissions:

r (Read) = 4
w (Write) = 2
x (Execute) = 1
Permission Examples
chmod 755 file (rwxr-xr-x): Owner has full control (7), Group can read/execute (5), Others can read/execute (5). Standard for scripts.
chmod 644 file (rw-r--r--): Owner can read/write (6), Group can read (4), Others can read (4). Standard for text files.
chmod 600 file (rw-------): Owner can read/write (6), Group gets nothing (0), Others get nothing (0). Standard for secret files (like SSH keys).
View permissions using: ls -l (e.g., -rwxr-xr--).

3. Managing Permissions & Ownership
chmod: Changes permissions.
Numeric: chmod 755 script.sh
Symbolic: chmod u+x file (Adds execute permission for the owner).
chown: Changes ownership.
chown user:group file
sudo: Runs a single command as the root user (e.g., sudo apt update).
/etc/sudoers: Controls who is allowed to use sudo. NEVER edit this file directly — use sudo visudo which checks for syntax errors before saving. A broken sudoers file can lock you out of the server permanently.
4. Cloud Security Context
Least Privilege: Service accounts must have minimal permissions. Regular users should not be able to read configuration files.
Auditing: Audit file permissions regularly. A common misconfiguration is leaving sensitive config files world-readable (chmod 644) when they should be restricted (chmod 600).
SSH Keys: Your ~/.ssh/ directory must be 700, and your private key (id_rsa) must be 600. If the permissions are too open, SSH will refuse to use the key.