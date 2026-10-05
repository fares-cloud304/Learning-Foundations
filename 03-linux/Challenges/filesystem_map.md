Overview
Unlike Windows, which uses drive letters (C:, D:), Linux uses a single unified tree starting from the root directory (/). All files, devices, and network shares are "mounted" into this single tree. As a Cloud Security Engineer, knowing where to find logs, configurations, and binaries is critical for incident response.

The Linux Filesystem Hierarchy
/├── bin/    # Essential user command binaries (ls, cd, grep, cat)├── sbin/   # System administration binaries (fdisk, reboot, iptables)├── etc/    # System and application configuration files (sshd_config, passwd)├── home/   # Personal files for regular users (e.g., /home/cloudpath)├── root/   # The home directory for the root (superuser) account├── var/    # Variable data (logs, databases, websites)│   └── log/  # System and application log files (auth.log, syslog)├── tmp/    # Temporary files (cleared on reboot)└── usr/    # User utilities and applications installed by the package manager
Cloud Security Context
/etc/passwd & /etc/shadow: Store user account information and password hashes. A prime target for attackers.
/var/log/auth.log: The first place an analyst looks to see failed or successful SSH login attempts.
/etc/ssh/sshd_config: The configuration file you edit to disable password login and secure SSH on a cloud server.