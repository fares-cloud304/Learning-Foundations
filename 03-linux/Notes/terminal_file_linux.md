Phase 3, Lessons 2 & 3: Terminal Navigation, File Manipulation & Permissions
Overview
Mastering the terminal is non-negotiable for a Cloud Security Engineer. You must be able to navigate the file system, manipulate files, and read logs without a graphical interface. Combining simple commands using pipes (|) and wildcards (*) allows you to automate complex security tasks instantly.

1. Navigation Commands
pwd : Print Working Directory (Where am I?).
ls -la : List all files (including hidden) in long format (shows permissions, owner, size).
cd /path : Change Directory (Absolute path - starts with /).
cd ~ : Go to the home directory.
cd .. : Go up one directory level.
cd - : Go back to the previous directory.
Pro Tip: Use Tab for auto-completion. Type cd /et + Tab to get cd /etc/.
2. File & Directory Manipulation
touch file.txt : Create a new empty file.
mkdir -p path/to/dir : Create a directory (and parent directories if they don't exist).
cp source dest : Copy a file (-r flag copies entire directories).
mv old new : Move or rename a file.
rm file : Delete a file (-r for directories, -f to force delete without prompting).
cat file : View entire file contents at once.
less file : Scroll through a large file (press q to quit).
head -20 file : View the first 20 lines.
tail -20 file : View the last 20 lines.
tail -f /var/log/auth.log : Follow a log file in real-time. Essential for monitoring live attacks.
3. Wildcards (Pattern Matching)
* : Matches any number of characters. (e.g., ls *.txt lists all text files).
? : Matches exactly one character. (e.g., ls file?.txt matches file1.txt but not file12.txt).
[abc] : Matches specific characters. (e.g., ls file[123].txt matches file1.txt).
4. Redirection & Pipes (The Power of Linux)
> : Redirects output to a file (Overwrites existing content).
>> : Redirects output to a file (Appends to existing content).
< : Reads input from a file.
| (Pipe) : Sends the output of one command as input to another.
Security Example: cat /var/log/auth.log | grep "FAILED" | wc -l
Prints the auth log -> filters for "FAILED" lines -> counts the number of failed logins.
5. File Permissions (Security Critical)
When you run ls -l, you see permissions like -rw-r--r--.

First 3 chars (rw-): Owner (User who created the file).
Second 3 chars (r--): Group (Users in the file's group).
Third 3 chars (r--): Others (Everyone else on the system).
Permission Letters: r = Read, w = Write, x = Execute.
Changing Permissions: Use chmod (Change Mode).
chmod 600 secret.txt : Owner gets read/write (6), Group gets nothing (0), Others get nothing (0).
chmod 755 script.sh : Owner gets full control (7), Group and Others can read and execute (5).