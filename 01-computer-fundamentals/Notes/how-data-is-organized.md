:

# Lesson 5 — How Data Is Organized


## 1. Filesystems


A filesystem is the way an operating system organizes and manages data stored on a device.


A filesystem organizes data into:


- Files — contain data
- Directories — organize files and other directories
- Paths — describe the location of files and directories


My home directory can be accessed with:


```bash
cd ~

~ represents the current user's home directory.

2. Hidden Files

In Linux, files and directories whose names begin with . are hidden by default.

Examples:

.bashrc
.bash_history
.profile
.config
.cache

Hidden does not mean encrypted, private, or secure.

It mainly prevents files from appearing in a normal directory listing.

Hidden files are commonly used for:

Configuration
User settings
Application data
Shell settings
Cached data

To show hidden files:

ls -a
3. Important Linux Commands
ls

Lists files and directories.

ls
ls -l

Shows files in long/detailed format.

It can show:

Permissions
Number of links
Owner
Group
File size
Modification time
Filename
ls -a

Shows all files, including hidden files.

ls -li

Shows detailed information and the inode number.

ls -li
-l = long/detailed format
-i = show inode number
cd

Changes the current directory.

cd ~
cat

Displays the contents of a file.

cat file.txt
rm

Removes a file/directory entry.

rm file.txt
ln

Creates a hard link.

ln original.txt hardlink.txt
ln -s

Creates a symbolic/soft link.

ln -s original.txt softlink.txt
echo

Prints text.

It can also be used with > to put text into a file:

echo "Hello" > file.txt
4. Inodes

An inode is a filesystem data structure that stores information about a file.

It can contain information such as:

File type
Permissions
Owner
File size
Timestamps
References to the file's data

A filename and an inode are not the same thing.

A directory entry connects a filename to an inode.

The inode number can be viewed with:

ls -li
5. Hard Links

A hard link is another filename/directory entry that points to the same inode as the original file.

Conceptually:

original.txt ───┐
                ├──> inode ──> file data
hardlink.txt ───┘

This means:

Both names refer to the same underlying file.
Both have the same inode number.
The data is shared.
Removing one filename does not necessarily remove the underlying data.

A hard link can be created with:

ln original.txt hardlink.txt
6. Symbolic / Soft Links

A symbolic link, also called a soft link, is a separate filesystem object that points to a pathname.

Conceptually:

softlink.txt ──> original.txt ──> inode ──> file data

A symbolic link has its own inode.

It does not directly point to the same inode as the target.

A symbolic link can be created with:

ln -s original.txt softlink.txt

If the target pathname is deleted or moved, the symbolic link can become a broken link.

7. Hard Links vs Soft Links
Hard Link	Soft/Symbolic Link
Points to the same inode	Points to a pathname
Same inode as the original	Has its own inode
Refers directly to the same underlying data	Refers to the target path
Can continue working after the original filename is removed	Can break when the target path is removed
Key rule
Hard link → same inode


Soft link → points to a path
8. Why Filesystem Organization Matters

Understanding how data is organized is important for cybersecurity because security work often involves examining:

Files
Directories
Hidden files
File permissions
File ownership
Inodes
Links
Configuration files
File locations

An attacker could potentially hide or manipulate files, so understanding how the filesystem works helps a security professional recognize unusual behavior.

9. Key Takeaways
A filesystem organizes and manages stored data.
Files contain data while directories organize files.
Files beginning with . are hidden by default in Linux.
Hidden does not mean secure or encrypted.
ls -a shows hidden files.
ls -li can show inode numbers.
An inode stores important information about a filesystem object.
A filename is associated with an inode through a directory entry.
A hard link points to the same inode.
A symbolic link points to a pathname.
Removing the original filename does not necessarily destroy data referenced by a hard link.
A symbolic link can become broken if its target path no longer exists.
Understanding filesystem organization is important for cybersecurity and system investigation.