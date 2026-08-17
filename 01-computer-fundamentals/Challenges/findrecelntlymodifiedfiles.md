:

# Challenge 2 — Find Recently Modified Files


## Task


Find all files on the system modified within the last hour and explain how this could be useful in security.


## Command Used


```bash
find / -type f -mmin -60 2>/dev/null
What I Learned
find searches for files and directories.
/ tells find to start searching from the root of the filesystem.
-type f tells it to search for regular files only.
-mmin -60 means files modified less than 60 minutes ago.
2>/dev/null hides permission-denied error messages.
Security Use

Searching for recently modified files can help a security analyst investigate unexpected changes to a system.

For example, an attacker might modify a configuration file, script, or other system file. Finding recently modified files can help identify what changed and when.

However, a recently modified file is not automatically malicious because normal system activity also modifies files.

Key Takeaway

I learned that find can search the filesystem using conditions such as file type and modification time. I don't need to memorize every option; I need to understand what the command is doing and know how to look up the correct options when needed.