:

# Lesson 6 — Linux Terminal & File Navigation


## 1. Terminal, Shell, and Command Prompt


### Terminal
The terminal is the application where I type commands.


Examples:
- Terminal.app
- Windows Terminal


### Shell
The shell is the program that interprets the commands I type.


Common shells:
- Bash — very common on Linux
- Zsh — default on macOS
- Fish — user-friendly shell
- PowerShell — commonly used on Windows


### Command Prompt
The command prompt is the text showing that the shell is ready for my input.


Example:


```text
user@host:~$
2. Navigating the Filesystem
pwd

Print working directory — shows where I currently am.

pwd
ls

Lists files and directories in the current directory.

ls
cd

Changes directory.

cd /var/log
cd ..

Moves up one directory.

cd ..
cd ~

Returns to my home directory.

cd ~
cd /

Moves to the root directory.

cd /
3. Creating and Managing Files
mkdir

Creates a directory.

mkdir folder_name
touch

Creates an empty file.

touch file.txt
cp

Copies a file or directory.

cp file.txt copy.txt
mv

Moves or renames a file or directory.

mv old.txt new.txt
rm

Removes a file.

rm file.txt
rm -r

Removes a directory recursively.

rm -r folder_name

⚠️ Be careful with rm, especially recursive deletion.

rm -rf

Forcefully removes files/directories recursively.

rm -rf folder_name

⚠️ Extremely dangerous if used on the wrong path. Never randomly use commands such as:

rm -rf /
4. Viewing File Contents
cat

Displays the contents of a file in the terminal.

cat file.txt
less

Views a file one page at a time.

less file.txt
head

Shows the beginning of a file.

head file.txt
tail

Shows the end of a file.

tail file.txt
5. Important Security Connection

The terminal gives me direct control over the filesystem and operating system.

Some commands can:

Find files
Create files
Move files
Delete files
Read files
Navigate through the filesystem

Because these commands can directly affect a system, I need to understand what a command does before running it.

Key Takeaways
The terminal is the application where I enter commands.
The shell interprets those commands.
The command prompt shows that the shell is ready for input.
pwd tells me where I am.
ls shows what is inside the current directory.
cd lets me navigate between directories.
~ represents my home directory.
/ represents the root of the filesystem.
mkdir creates directories.
touch creates empty files.
cp copies files/directories.
mv moves or renames files/directories.
rm deletes files.
cat, less, head, and tail let me inspect file contents.