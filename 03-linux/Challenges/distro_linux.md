Lab: Linux Distribution (Distro) Research
Overview
Linux is not a single operating system, but a kernel combined with different tools, package managers, and interfaces to create "Distributions" (Distros). As a Cloud Security Engineer, you will encounter multiple distros. Understanding their primary use cases ensures you select the right tool for the job.

1. Ubuntu
Package Manager: apt
Primary Use Case: General-purpose cloud computing, beginners, and AWS EC2 instances.
Why it matters: Ubuntu is the most popular Linux distribution for the cloud due to its massive community, extensive documentation, and ease of use. When launching a virtual machine on AWS (an EC2 instance), Ubuntu is often the default AMI (Amazon Machine Image) chosen by developers.
2. Alpine Linux
Package Manager: apk
Primary Use Case: Docker containers and lightweight virtual machines.
Why it matters: Alpine Linux is incredibly tiny (around 5MB). In cloud security, attack surface matters. Because Alpine strips out almost all unnecessary tools and libraries, it has a much smaller attack surface than a full Ubuntu installation. It is the industry standard for building secure, minimal Docker images.
3. Kali Linux
Package Manager: apt
Primary Use Case: Penetration testing and offensive security.
Why it matters: Kali comes pre-installed with over 600 penetration testing tools (like Nmap, Metasploit, Wireshark, and Burp Suite). Cloud security engineers use Kali to simulate attacks against their own AWS infrastructure to find vulnerabilities before real attackers do.