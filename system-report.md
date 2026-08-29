# System Report

## 1. Hardware

I used the `lscpu` command to inspect the CPU available to my system. The result showed an AMD Ryzen 5 5600 6-Core Processor with 12 logical CPUs, 6 physical cores, and 2 threads per core. The system uses the x86_64 architecture and supports both 32-bit and 64-bit CPU operation.

The output also showed AMD-V virtualization support. Because I am using WSL2, the hypervisor vendor is Microsoft and the virtualization type is full. This shows how my normal Windows computer can provide a virtual Linux environment.

A CPU executes program instructions. Physical cores can work on separate tasks, while threads allow each core to handle more than one stream of work. In cloud computing, a virtual machine receives virtual CPUs instead of directly owning a physical CPU.

## 2. Memory and Storage

I used `free -h` to inspect memory. The result showed approximately 15 GiB of total memory, about 818 MiB used, and about 14 GiB available. The system also has 4 GiB of swap, with 0 bytes currently being used.

RAM is temporary working memory used by running programs. Swap is disk space that can be used when RAM becomes full, but it is slower than RAM. Since no swap is being used, the system is not currently under memory pressure.

I used `df -h` to inspect storage. The main WSL file system mounted at `/` has about 1007 GiB of size, about 2 GiB used, and about 954 GiB available. The Windows C: drive is mounted at `/mnt/c` with 238 GiB total and 61% used. The G: drive is mounted at `/mnt/g` with 693 GiB total and 44% used.

The WSL file system has plenty of available storage. The C: drive is more important to watch because it is already 61% full. If a disk becomes full, applications may fail and system availability can be affected.

## 3. Operating System and Kernel

I first typed `cat /etc/os-realease`, but the command failed because I misspelled `release`. I corrected it and ran `cat /etc/os-release` successfully.

The system is running Ubuntu 26.04 LTS with the codename Resolute Raccoon. Ubuntu is a Linux distribution based on Debian.

The `uname -a` command showed this kernel information:

```text
Linux DESKTOP-KK6K4IM 6.18.33.2-microsoft-standard-WSL2 x86_64 GNU/Linux
```

This confirms that the Linux environment is running inside WSL2 and uses a Microsoft WSL2 kernel. The kernel is the core part of the operating system. It manages hardware resources and provides services to applications through system calls.

The terminal programs and other applications run in user space. They do not normally access hardware directly. They request services from the kernel, such as reading a file or using the network, through system calls.

## 4. Boot Information

The project asks me to investigate boot information with `dmesg` and `journalctl -b`. I have not captured those command results yet, so this section is not complete.

The purpose of `dmesg` is to show kernel messages, including hardware detection and device initialization. The command `journalctl -b` shows system logs from the current boot. These logs can help explain which services started, which services failed, and whether anything unusual happened during startup.

## 5. My Explanation

My system has a physical AMD CPU, but Linux is running through WSL2 as a virtualized environment. This connects the computer fundamentals lesson to cloud computing: a cloud EC2 instance also uses virtual hardware provided by a physical data center server.

The CPU provides processing power, RAM holds active program data, and storage keeps data for longer periods. The operating-system kernel manages these resources. The command results show that my current system has enough memory and storage for basic cloud-engineering practice, while the Windows C: drive should be monitored because it is more than half full.

The most important thing I learned is that command output is evidence, but I must explain what the evidence means. In a cloud environment, the same process could be used to investigate a virtual server before troubleshooting performance or security problems.

## Evidence Commands Used

```text
lscpu
free -h
df -h
uname -a
cat /etc/os-release
dmesg | head -30
journalctl -b | head -30
```

## Notes

I did not include every line from the command output because some lines contain machine-specific information that is not necessary for the explanation. I should keep public GitHub reports focused on useful evidence and avoid exposing unnecessary personal or system details.
