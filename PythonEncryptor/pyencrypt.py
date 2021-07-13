#!/usr/bin/env python3

# Script: Ops Challenge 06 File Encryption
# Author: Ray Caoagdan
# Date of Last Revision: 07/112021
# Purpose: Encryption with Python


##############################################################################
# Import Library 
##############################################################################
import base64
import builtins
from os import path
from cryptography.fernet import Fernet 

##############################################################################
# Main Menu Fuction
##############################################################################
def main_menu():
    print (" ")
    print ("What would you like to do? ")
    print("1.Encrypt a file")
    print("2.Decrypt a file")
    print("3.Enrypt a message")
    print("4.Decrypt a messsage")
    mainResponse = input("Desired Request:")
    if mainResponse == '1':
        fileEncryption()
    elif mainResponse == '2':
        fileDecryption()
    elif mainResponse == '3':
        msgEncryption()
    elif mainResponse == '4':
        msgDecryption()
    else:
        print("Incorrect selection main")
        main_menu()

##############################################################################
# Key Generation 
##############################################################################
def writeKey():
    key = Fernet.generate_key()
    with open('filekey.key','wb') as key_file:
        key_file.write(key)

##############################################################################
# loads key
##############################################################################
def loadKey():
   return open('filekey.key', 'rb').read()

##############################################################################
# keys to be used in fuctions
##############################################################################
writeKey()
key=loadKey()
fK=Fernet(key)
##############################################################################
# File Encryption 
##############################################################################
def fileEncryption():
    print("FILE ENCRPYTION \n")
    filePath = input("File to Encrpyt:")
    with open(filePath, 'rb') as file:
        originalFile = file.read()
    eFile = fK.encrypt(originalFile)
    with open(filePath,'wb') as encryptedFile:
        encryptedFile.write(eFile)
    encryptedFile.close()
    main_menu()

##############################################################################
# File Decryption
##############################################################################
def fileDecryption():
    print("FILE DECRYPTION \n")
    filePath = input("File to Decrypt:")
    with open(filePath, 'rb') as enc_File:
        originalFile = enc_File.read()
    dFile = fK.decrypt(originalFile)
    
    with open(filePath,'wb') as dec_File:
        dec_File.write(dFile)
    dec_File.close()
    main_menu()

##############################################################################
# Message Encryption
##############################################################################
def msgEncryption():
    print(" ")
    print("Message Encryption \n")
    user_msg = input("MESSAGE TO ENCRYPT:")
    msg_bytes = user_msg.encode('ascii')
    encodedMSG=base64.b64encode(msg_bytes)
    print(" ")
    print("Encoded Message:")
    print(encodedMSG)

##############################################################################
# Message Decryption
##############################################################################
def msgDecryption():
    print(" ")
    print("Message Decryption \n")
    udmsg = input("MESSAGE TO DECRYPT:")
    b64_bytes = udmsg.encode('ascii')
    msg_bytes = base64.b64decode(b64_bytes)
    oMsg=msg_bytes.decode('ascii')
    print(" ")
    print(oMsg)
    print("Decrypted Message:")
    main_menu()
##############################################################################
# Main
##############################################################################
main_menu()

##############################################################################
# End
##############################################################################


##############################################################################
# Sources
##############################################################################
## https://stackabuse.com/encoding-and-decoding-base64-strings-in-python
## https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
## https://pypi.org/project/cryptography/
##############################################################################
# End Sources 
##############################################################################