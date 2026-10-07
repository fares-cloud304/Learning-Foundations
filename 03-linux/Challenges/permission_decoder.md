Lab: Permission Decoder
Overview
Linux permissions are calculated using a simple math formula based on three numbers:

Read (r) = 4
Write (w) = 2
Execute (x) = 1
You add these numbers together for each of the three categories: Owner, Group, and Others.

Decoding the Permissions
1. 755 (rwxr-xr-x)
Owner (7): Read + Write + Execute (4+2+1)
Group (5): Read + Execute (4+0+1)
Others (5): Read + Execute (4+0+1)
Use Case: This is the standard permission for executable scripts or public web directories. The owner has full control, everyone else can run/read it but cannot modify it.
2. 644 (rw-r--r--)
Owner (6): Read + Write (4+2+0)
Group (4): Read only (4+0+0)
Others (4): Read only (4+0+0)
Use Case: Standard permission for regular files (like text files or public documents). The owner can edit, everyone else can only read.
3. 600 (rw-------)
Owner (6): Read + Write (4+2+0)
Group (0): No access (0)
Others (0): No access (0)
Use Case: This is the standard permission for private files. Only the owner can read or modify the file. Nobody else on the system can see what is inside it.
4. 777 (rwxrwxrwx)
Owner (7): Read + Write + Execute (4+2+1)
Group (7): Read + Write + Execute (4+2+1)
Others (7): Read + Write + Execute (4+2+1)
Use Case: NEVER USE THIS. This gives every single user on the system full control over the file. Any compromised account can modify or delete the file.
Conclusion: Most Secure for a Private File?
The most secure permission for a private file (like an AWS Secret Key or a private SSH key) is 600.

If you want to completely freeze a file so nobody (not even the owner) can touch it without unlocking it first, you use 000.

