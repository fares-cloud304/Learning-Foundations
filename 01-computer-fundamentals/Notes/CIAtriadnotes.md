Lesson 9 — CIA Triad & Threat Modeling
 CIA Triad

The CIA Triad is a fundamental cybersecurity model used to think about the three main security goals of a system.

Confidentiality

Goal: Prevent unauthorized people from accessing information.

Ask:

Who is allowed to see this information?

Examples:

Encryption
Access controls
Passwords
Authentication
Key management

Example: A hacker steals a user's banking password and accesses their account information.

→ Confidentiality is compromised.

Integrity

Goal: Keep information accurate, trustworthy, and protected from unauthorized modification.

Ask:

Has the information been changed improperly?

Examples:

Hashes
Digital signatures
Immutable logs
File integrity monitoring
Checksums

Example: An attacker changes a bank transaction from $100 to $1,000.

→ Integrity is compromised.

Availability

Goal: Make sure systems and information are accessible when legitimate users need them.

Ask:

Can authorized users access the system when they need it?

Examples:

Backups
Redundancy
Failover
Load balancing
DDoS protection
Auto Scaling

Example: A DDoS attack overwhelms a banking website and customers cannot access it.

→ Availability is compromised.

 CIA Quick Reference
Component	Main Question	Example Attack
Confidentiality	Who can see it?	Stolen credentials
Integrity	Has it been changed?	Modified transaction
Availability	Can I access it?	DDoS attack
Memory trick
C → Can unauthorized people SEE it?
I → Is the information still correct?
A → Are authorized users ABLE to access it?
