Lesson 9 Notes: Dictionaries & Sets
Phase: 2 - Python Programming
Status: ✅ Completed

1. Dictionaries (The Core Data Structure)
A dictionary maps keys to values. It is the primary way AWS APIs return data (JSON).

Syntax & Access
config = {"host": "localhost", "port": 443, "debug": False}config["port"]  # Returns 443
Modifying
Add/Update: config["timeout"] = 30
Delete: del config["debug"]
Check Exists: if "port" in config:
Iteration Methods
.keys(): Returns all the keys.
.values(): Returns all the values.
.items(): Returns (key, value) pairs (Crucial for loops).
python

for key, value in config.items():
    print(f"{key}: {value}")
Cloud Use Case
Dictionaries model everything in cloud security:

user = {"name": "alice", "role": "admin", "mfa": True}
vuln = {"cve": "CVE-2024-1234", "severity": "high", "affected": ["server1", "server2"]}
2. Sets (The Deduplication Engine)
A set is an unordered collection of unique items. It automatically removes duplicates.

Syntax
python

tags = {"critical", "verified", "patched"}
Deduplication
Converting a list to a set instantly removes copies:

python

set([1, 1, 2, 2, 3]) # Becomes {1, 2, 3}
Set Math (Powerful for Security)
Union (|): All items in either set.
Intersection (&): Items only in BOTH sets.
Example: allowed_users & current_users (Who is allowed AND currently logged in?)
Difference (-): Items in the first set but NOT the second.
Speed Advantage
Checking if an item exists in a Set (if ip in blocked_set:) is O(1) (instant). Checking a List is O(n) (has to search one by one). For 10,000 IPs, Sets are thousands of times faster.

Cloud Use Case
Managing blocked IP addresses. blocked_ips.add(ip) — adding the same IP twice only keeps one copy, preventing redundant firewall rules.

3. Nested Structures (The Reality of APIs)
Real security data is rarely flat. It is nested: lists inside dictionaries, dictionaries inside dictionaries.

Example
python

scan_results = {
    "server1": {"ports": [22, 80, 443], "os": "Ubuntu"}, 
    "server2": {"ports": [22], "os": "CentOS"}
}
Deep Access
You chain brackets to dig into the layers:

python

scan_results["server1"]["ports"][0]  # Gives 22
Deep Iteration
Use .items() to loop through the top level, then access the nested keys:

python

for server, info in scan_results.items():
    print(f"Server: {server}, Open Ports: {info['ports']}")
Cloud Use Case
Understanding nested structures is crucial for working with JSON API responses. AWS boto3 returns heavily nested dictionaries. You must know how to dig through them to extract InstanceId or State data.