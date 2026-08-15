AppArmor
What is AppArmor?

AppArmor is a Linux security system that restricts what applications and processes are allowed to do.

It uses security profiles that define what a particular application can access, such as certain files, directories, or capabilities.

How does it enhance kernel security?

AppArmor works with the Linux kernel to enforce these restrictions.

So even if an application is compromised, AppArmor can restrict what that application is able to access.

For example:

Application
     ↓
AppArmor restrictions
     ↓
Linux kernel
     ↓
Files / resources

The important idea is that AppArmor provides an additional layer of protection beyond normal Linux permissions.

Why is it useful?

If an attacker compromises an application, they may try to use that application to access other files or resources.

AppArmor can limit what that application is allowed to access, which can reduce the potential damage from a compromise.

What I learned

AppArmor is a Linux security system that uses profiles to control what applications can access. It works with the kernel to enforce these restrictions and adds another security layer. This can help limit the damage if an application is compromised.