.

# Challenge 2: Hard Links vs Soft Links


## Goal


Create a hard link and a soft (symbolic) link to the same file, delete the original file, and observe what happens.


## Step 1 — Create a file


```bash
echo "Hello filesystem" > original.txt

This created original.txt containing:

Hello filesystem
Step 2 — Create a hard link
ln original.txt hardlink.txt

A hard link creates another filename that points to the same inode as the original file.

Step 3 — Create a soft link
ln -s original.txt softlink.txt

A soft/symbolic link points to the pathname of the original file.

Step 4 — Check the inode numbers
ls -li

I found:

44928 ... hardlink.txt
44928 ... original.txt
44943 ... softlink.txt -> original.txt

The hard link and original file had the same inode number (44928), while the soft link had a different inode.

Step 5 — Delete the original
rm original.txt

rm removes the file/directory entry.

Step 6 — Test the hard link
cat hardlink.txt

Output:

Hello filesystem

The hard link still worked because it pointed to the same inode and the file data still existed.

Step 7 — Test the soft link
cat softlink.txt

Output:

cat: softlink.txt: No such file or directory

The soft link was broken because it pointed to original.txt, which had been deleted.

What I Learned
A hard link is another name pointing to the same inode.
A soft link points to a pathname.
Hard links can still work after the original filename is deleted.
A soft link becomes broken when the path it points to no longer exists.
ls -li can be used to inspect inode numbers.
rm removes a file/directory entry.
ln creates a hard link.
ln -s creates a symbolic/soft link.