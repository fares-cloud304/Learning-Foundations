Phase 2, Lesson 11: Modules & Packages
Overview
Transitioning from writing isolated scripts to building reusable security toolkits. Modules and packages are how professional cloud security engineers organize code and leverage third-party libraries like boto3 and requests.

1. The Python Standard Library
Python comes with a massive pre-installed library. No pip install required.

import os (Operating system interactions)
import sys (System-specific parameters)
import json (JSON parsing - essential for AWS API responses)
import socket (Networking/port scanning)
import hashlib (Hashing - SHA-256 for file integrity)
import subprocess (Executing shell commands from Python)
Syntax:

import module_namemodule_name.function()# Or import specific items:from module_name import function
2. Creating Your Own Modules & Packages
Any .py file is a module. If you have security_utils.py, another script can import security_utils and use its functions.

Professional Project Structure (Package):

text

mysecurity/
├── __init__.py
├── scanners.py
├── parsers.py
└── reporters.py
Usage:

python

from mysecurity.scanners import port_scan
3. PyPI & pip (External Packages)
pip installs packages from PyPI (Python Package Index) — a repository of 400,000+ packages.

Essential Cloud Security Packages:

requests (HTTP API interactions)
boto3 (AWS SDK)
paramiko (SSH automation)
scapy (Packet manipulation)
cryptography (Encryption)
python-nmap (Port scanning)
Dependency Management Commands:

bash

pip install requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt