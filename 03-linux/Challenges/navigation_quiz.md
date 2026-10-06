Lab: Navigation Quiz
Objective
Starting from /home/user, navigate to the system log directory, list the files inside it, and return back to the home directory using exactly 4 commands.

The Solution (4 Commands)
# 1. Navigate to the var/log directory using an absolute pathcd /var/log# 2. List all files in the directory (using -la for long format and hidden files)ls -la# 3. Return to the home directory using the tilde shortcutcd ~
Why this matters for Cloud Security
As an incident responder, you will often need to jump from a user's home directory (/home/user) straight to the log directories (/var/log) to check for brute-force attacks, and then immediately jump back to the user's directory to inspect their files. Using absolute paths (/var/log) and shortcuts (~) makes this instant.