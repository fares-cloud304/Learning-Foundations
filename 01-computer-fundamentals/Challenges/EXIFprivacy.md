EXIF Privacy: Inspecting and Removing Photo Metadata


A practical cybersecurity note on why photo metadata matters, how to inspect it with ExifTool, and how to remove metadata before sharing an image.

Challenge

Research how to strip EXIF data from photos before sharing them. Why is this important?

For this challenge, I inspected a JPEG photo using ExifTool:

Bash


exiftool /mnt/g/Downloads/photo.jpeg



What I Did

I used the exiftool command to examine the metadata and technical properties stored in photo.jpeg. The command performed an inspection only; it did not delete or modify the image.

The file was located at:

Plain Text


/mnt/g/Downloads/photo.jpeg



ExifTool reported that the file was a valid JPEG image with a size of 130 kB and dimensions of 972 × 1296 pixels.

Important Parts of the Output

Output field
Meaning
File Type: JPEG
The file’s detected format is JPEG
File Type Extension: jpg
The standard extension associated with the detected format is .jpg
MIME Type: image/jpeg
Applications identify the file as a JPEG image using this media type
Image Width: 972
The image is 972 pixels wide
Image Height: 1296
The image is 1296 pixels high
Image Size: 972x1296
The image dimensions are 972 by 1296 pixels
Megapixels: 1.3
The image contains approximately 1.3 million pixels
Bits Per Sample: 8
Each color sample uses 8 bits
Color Components: 3
The image uses three color components, commonly representing color channels
Encoding Process: Baseline DCT, Huffman coding
The JPEG uses a standard lossy-compression encoding process
File Modification Date/Time
The filesystem’s recorded modification time, not necessarily the moment the photo was taken
File Permissions
The access permissions reported for the file on the operating system




The displayed output did not show fields such as GPS Latitude, GPS Longitude, Camera Model Name, or Date/Time Original. This means those fields were not present in the output shown. However, metadata can vary between files, so it is good practice to inspect every image before sharing it.

What Is EXIF Data?

EXIF, or Exchangeable Image File Format, is metadata associated with image files. It can describe how, when, and where a photograph was captured.

Depending on the device and application, EXIF metadata may include:

•
GPS coordinates or location information

•
The date and time the photograph was taken

•
Camera manufacturer and model

•
Lens and camera settings

•
Orientation and dimensions

•
Editing software

•
Copyright or author information

Some of the fields shown by ExifTool, such as file permissions and file modification time, describe the file in the operating system rather than the camera’s EXIF data. This distinction is important when interpreting command output.

Why Is EXIF Privacy Important?

Photo metadata can reveal information that is not visible in the image itself. If a photograph contains GPS coordinates, someone who receives the file may be able to determine where it was taken. This can expose a home address, workplace, school, travel destination, or another sensitive location. Apple’s personal safety guidance specifically warns that shared photos containing location metadata may allow recipients to learn where the photo was taken.[1]

Metadata can also reveal the device used to create the image, when it was captured, and which software edited it. This information may be harmless in some situations, but it can create unnecessary privacy exposure when posting photos publicly, sending them to unknown people, or uploading them to websites.


Privacy principle: The visible image is not always the complete file. Metadata may contain sensitive information outside the pixels themselves.

