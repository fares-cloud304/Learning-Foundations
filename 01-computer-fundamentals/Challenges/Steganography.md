Steganography and Malware Command-and-Control


A short study note explaining a benign steganography experiment and how malware can abuse hidden data for command-and-control (C2).

Challenge

Research how steganography is used by malware for command-and-control and explain one technique.

What I Did

First, I created a text file containing a test message:

Bash


echo "This is my hidden test message." > secret.txt
cat secret.txt



The output confirmed that the file contained:

Plain Text


This is my hidden test message.



I then embedded the text file inside a JPEG image using steghide:

Bash


steghide embed -cf /mnt/g/Downloads/photo.jpeg -ef secret.txt



After entering a passphrase, the tool reported:

Plain Text


embedding "secret.txt" in "/mnt/g/Downloads/photo.jpeg"... done



Finally, I inspected the image:

Bash


steghide info /mnt/g/Downloads/photo.jpeg



The results showed that the JPEG had approximately 7.2 KB of capacity and contained an embedded file named secret.txt. The embedded data was 32 bytes, compressed, and encrypted using Rijndael-128 in CBC mode.

What Happened and Why?

The JPEG still looked like an ordinary image, but it now carried an additional hidden file. Steganography hides the existence of data inside another file, while encryption protects the hidden data from being read without the passphrase.

This was a benign laboratory experiment. I placed a short text message inside an image to demonstrate how hidden data can be embedded and detected.

One Malware C2 Technique: Commands Hidden in Images

A malware operator can use a similar concept for covert command-and-control. The infected computer may periodically download an ordinary-looking image from a website, email account, or public service. The malware then extracts hidden data from the image and interprets it as a command or configuration update.

For example, a hidden message could instruct the malware to change its communication settings or retrieve another file. The malware could also hide collected information inside an image before sending it back to the operator. Because the network request may look like a normal image download, this technique can make C2 traffic harder to identify.

MITRE ATT&CK documents this behavior as T1001.002: Data Obfuscation—Steganography. Its examples include malware that receives commands appended to image files or processes steganographic images exchanged through email.[1]

Why This Matters

Steganographic C2 matters because traditional monitoring may focus on visible text, obvious malicious domains, or suspicious protocols. A hidden command inside a normal-looking media file may be more difficult to detect.

Defenders can look for unusual patterns, such as image files being repeatedly downloaded after suspicious process activity, unexpected use of tools such as steghide, or media files that are modified and then sent to external systems.[1]


Conclusion: My experiment demonstrated how a message can be hidden inside a JPEG. Malware can abuse the same idea by hiding C2 commands or stolen data in ordinary-looking images, making steganography an important technique for security analysts to understand.

