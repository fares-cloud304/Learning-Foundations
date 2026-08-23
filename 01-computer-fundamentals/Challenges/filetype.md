Challenge: Renaming a Text File to .jpg

Challenge Question


Rename a .txt file to .jpg and use the file command on it. What happens and why?

Commands Used

The file was renamed so that its filename ended in .jpg, and then the following command was run in WSL/Linux:

Bash


file /mnt/g/Downloads/faresmsalah4.jpg



The result was:

Plain Text


/mnt/g/Downloads/faresmsalah4.jpg: ASCII text, with CRLF line terminators



The raw contents were then examined with:

Bash


hexdump -c /mnt/g/Downloads/faresmsalah4.jpg | head



The output was:

Plain Text


0000000   f   a   r   e   s   m   s   a   l   a   h   4  \\r  \\n   f   a
0000010   r   e   s   1   2   3
0000016



What Happened?

Changing the filename from something such as file.txt to faresmsalah4.jpg changed only the file extension. It did not convert the contents of the file into JPEG image data.

The file command identified the file as ASCII text, not as a JPEG image. This happened because file examines the content of the file—especially its file signature or other recognizable patterns—instead of trusting the filename extension.

The hexdump output confirms this result. It displays readable characters such as:

Plain Text


f a r e s m s a l a h 4
f a r e s 1 2 3



These characters are the text stored inside the file. The symbols \\r and \\n represent carriage return and line feed, respectively. Together, they indicate Windows-style line endings, which is why file reported CRLF line terminators.

Why Did This Happen?

A file extension is only a label used by the operating system and applications. Renaming a text file to .jpg does not rewrite its bytes, add JPEG headers, or perform image conversion.

A genuine JPEG normally begins with a recognizable JPEG file signature, commonly represented in hexadecimal as:

Plain Text


FF D8 FF



Your file instead begins with the ASCII bytes for the characters f, a, r, e, and so on. Therefore, the content does not match the structure of a JPEG image, even though the filename ends in .jpg.

Observation
Meaning
Filename ends in .jpg
Only the name was changed; this does not prove the file is an image
file reports ASCII text
The actual contents are readable text
CRLF line terminators
The text uses Windows-style line endings
hexdump shows readable letters
The file contains text bytes rather than JPEG image data
No JPEG signature is detected
The file is not a valid JPEG merely because of its extension




Security Lesson

This challenge demonstrates why security analysts should not trust file extensions. A malicious file could be renamed from one extension to another to disguise its real format, or a harmless text file could be given an image extension without actually becoming an image.

The file command helps verify the file’s actual type by inspecting its contents. The hexdump command provides a lower-level view of those contents, allowing an analyst to inspect the raw bytes and identify readable text or file signatures.


Conclusion: Renaming a .txt file to .jpg changes the filename, not the file format. The file remains ASCII text because its underlying bytes are still text, and file correctly identifies the content rather than trusting the misleading .jpg extension.

