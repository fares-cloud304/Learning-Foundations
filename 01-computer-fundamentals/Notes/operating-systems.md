# Lesson 4 — Operating Systems

## What is an Operating System?

An operating system (OS) is the software that manages the computer's hardware and provides an environment for applications to run.

Examples:
- Windows
- macOS
- Linux

## Kernel

The kernel is the core part of an operating system.

It manages communication between applications and the hardware/resources of the computer.

## User Space

User space is where normal applications run.

Applications normally cannot directly control hardware. They request services from the kernel.

## System Calls

System calls are the way applications request services from the operating system's kernel.

Basic model:

Application → System Call → Kernel → Hardware/Resource

## Windows

- Closed-source operating system.
- Developed by Microsoft.
- Very common on desktop computers.
- Frequently targeted by malware.

## macOS

- Closed-source operating system.
- Developed by Apple.
- Built on a Unix-based foundation.
- Designed with strong platform security controls.

## Linux

- Open-source operating system.
- Has many distributions, such as Ubuntu, Debian, and others.
- Provides strong permissions and security features.
- Commonly used for servers and cloud infrastructure.
- Very important for cloud security.

## Linux Security

Important Linux security concepts include:
- File permissions
- User accounts
- SELinux
- AppArmor
- Regular updates and patching

## Linux Commands I Learned

### `ls`

Lists files and directories in the current directory.

```bash
ls
cat filename :Displays the contents of a file.
uname -r : Displays the Linux kernel version.
strace ls : Allows you to observe the system calls made by a program.
strace -c ls : Provides a summarized table of the system calls made by a program.


What I Learned From the strace Challenge

Different programs make different system calls because they perform different tasks.

ls lists the contents of directories, while cat reads and displays file contents.

For example, ls used getdents64 to retrieve directory entries, while cat primarily used calls such as read to read file contents.

The important concept is:

Application → System Calls → Kernel → Resources

Key Takeaways
The OS manages hardware and provides services to applications.
The kernel is the core of the OS.
Applications use system calls to communicate with the kernel.
Linux is particularly important for cloud infrastructure.
ls lists files and directories.
cat displays file contents.
strace lets me observe system calls.
Different applications make different system calls depending on what they need to do.