## Overview
Encryption of data at rest is a common need in security operations. Today you will begin development of a Python script that encrypts a single file.

### Requierments

***Part 1:***

In Python, create a script that utilizes the cryptography library to:

* Prompts user to select a mode:
    * Encrypt a file
    * Decrypt a file
    * Encrypt a message
    * Decrypt a message

* If mode 1/2 selected user provides a filepath
* If mode 3/4 selected user provides cleartext string

Depending on the selection, perform one of the below functions. You’ll need to create four functions:

* Encrypt the target file if in mode 1.
    * Delete the existing target file and replace it entirely with the encrypted version.

* Decrypt the target file if in mode 2.
    * Delete the encrypted target file and replace it entirely with the encrypted version.

* Encrypt the string if in mode 3.
    * Print the ciphertext to the screen.

* Decrypt the string if in mode 4.
    * Print the cleartext to the screen.   

***Part 2:***

* Recursively encrypt a single folder and all its contents.
* Recursively decrypt a single folder that was encrypted by this tool.

***Part 3:***
* Alter the desktop wallpaper on a Windows PC with a ransomware message
* Create a popup window on a Windows PC with a ransomware message

### Stretch Goals
* Prompt the user if the output file should be compressed to an archive.
* If the user responds ‘y’ for yes, compress the resulting file to an archive. Refer to How to Compress and Decompress Files in Python or use the os library to perform OS-specific archival commands.

