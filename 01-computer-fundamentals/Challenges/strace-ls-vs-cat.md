# Challenge: Compare `ls` vs `cat` with `strace`

## Goal

Use `strace` to observe and compare the system calls made by `ls` and `cat`.

## Commands Used

```bash
strace -c ls
strace -c cat /etc/hostname




Results
ls

Total system calls: 143

Important calls I observed:

getdents64 — 2 calls
statx — 6 calls
openat — 12 calls
read — 18 calls
close — 11 calls

ls uses system calls to access a directory, retrieve directory entries, get file/directory information, and display the results.

cat

Total system calls: 142

Important calls I observed:

read — 18 calls
openat — 12 calls
close — 13 calls
statx — 5 calls
splice — 4 calls

cat uses system calls to open a file, read its contents, and output the contents.

Differences

The biggest difference I noticed was that ls used getdents64, while cat did not.

getdents64 is used to retrieve directory entries, which makes sense because ls needs to find the contents of a directory.

cat used splice in my test and mainly focused on reading and outputting file contents.

What I Learned

Different programs make different system calls depending on what they need to do.

ls needs to interact with directories and their entries, while cat needs to read the contents of a file.

strace allows me to see how a program communicates with the Linux kernel through system calls.