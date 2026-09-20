Lesson 10 Notes: File I/O & Error Handling
Phase: 2 - Python Programming
Status: ✅ Completed

1. File I/O (Reading and Writing)
Programs need to save data permanently. Without files, your data disappears when the script ends.

The open() Function & Modes
"r": Read mode (default). Loads file data into memory.
"w": Write mode. Overwrites the entire file (Destructive!).
"a": Append mode. Adds new data to the end without deleting existing data.
Reading Data
# Read entire file into one giant stringwith open("log.txt", "r") as f:    content = f.read()# Read line-by-line (Crucial for massive log files to save RAM)with open("log.txt", "r") as f:    for line in f:        print(line.strip())
Writing Data
python

with open("report.txt", "w") as f:
    f.write("Vulnerability Scan Complete\n")
2. The with Statement (Context Managers)
The with statement guarantees that resources are cleaned up, even if an error occurs.

Why it's mandatory:
If you use bare open(), you must remember f.close(). If you forget, the file stays "locked" in your computer's memory. Over time, this causes resource leaks that will crash long-running monitoring scripts.

Syntax
python

# The Professional Way (Auto-closes)
with open("file.txt", "w") as f:
    f.write("data")
# File is automatically closed here, even if the write failed!
Multiple Files
You can open multiple files in one block:

python

with open("input.txt") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read())
Rule: Never use bare open() without with. It is the Pythonic best practice.

3. Error Handling (try / except)
Programs crash when errors occur (file not found, network timeout, invalid input). try/except catches errors gracefully so your script can keep running.

The Problem
If an AWS API returns bad data, your script crashes and stops processing the other 99 servers.

The Solution
Tell Python to try a dangerous action. If an error happens, catch it and run a fallback plan.

Syntax
python

try:
    # Dangerous code
    f = open("missing.txt")
except FileNotFoundError:
    # Fallback plan for this specific error
    print("File not found! Skipping...")
Catching Specific Exceptions
Always catch specific errors first. Catching everything blindly hides bugs.

python

try:
    result = scan(host)
except TimeoutError:
    log(f"{host} timed out") # Network blip
except ValueError:
    log("Invalid data format") # Bad API data
except Exception as e:
    log(f"Unexpected Error: {e}") # Catch-all as last resort
The finally Block
Code inside finally always runs, whether the code succeeded or failed. It is used for mandatory cleanup (like closing connections).

python

try:
    connect_to_aws()
except ConnectionError:
    print("Connection failed")
finally:
    close_connection() # Always runs!
Cloud Engineering Context
File I/O
Security scripts constantly read and write files:

Read: Parsing AWS CloudTrail logs saved to your hard drive.
Write: Saving security reports to a .txt or .csv file for management.
Append: Adding ongoing debug logs to scanner.log without overwriting previous days.
Error Handling
AWS APIs fail constantly (rate limits, network blips, missing permissions). try/except is what separates amateur scripts from professional, resilient cloud automation.

If boto3 fails to connect to an EC2 instance, you catch the ConnectionError, log it, and move on to the next instance. The script survives.