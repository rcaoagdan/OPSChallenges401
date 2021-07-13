#!/usr/bin/env python3

# Script: Ops Challenge 06 File Encryption
# Author: Ray Caoagdan
# Date of Last Revision: 07/112021
# Purpose: Encryption with Python


##############################################################################
# Import Library 
##############################################################################
import base64 
import os
from cryptography.fernet import Fernet 

##############################################################################
# Main Menu Fuction
##############################################################################
def main_menu():
    print (" ")
    print ("What would you like to do? ")
    print("1.Encrypt a File")
    print("2.Decrypt a File")
    print("3.Encrypt a Folder")
    print("4.Decrypt a Folder")
    print("5.Enrypt a message")
    print("6.Decrypt a messsage")
    print("7.Exit")
    mainResponse = input("Desired Request:")
    if mainResponse == '1':
        fileEncryption()
    elif mainResponse == '2':
        fileDecryption()
    elif mainResponse== '3':
        folderEncrypt()
    elif mainResponse == '4':
        folderDecrypt()
    elif mainResponse == '5':
        msgEncryption()
    elif mainResponse == '6':
        msgDecryption()
    elif mainResponse == '7':
        exit
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
# Folder Encryption
##############################################################################
def folderEncrypt():
    print("Folder Encryption \n")
    folderInput = input("Folder to Encrypt:")
    for filename in os.listdir(folderInput):
        files = os.path.join(folderInput,filename)
        with open(files,'rb') as f:
            enc_data=f.read()
        eData = fK.encrypt(enc_data)
        with open(files,'wb') as eF:
            eF.write(eData)
        eF.close()
    main_menu()


##############################################################################
# Folder Decryption
##############################################################################
def folderDecrypt():
    print("Folder Decryption \n")
    folderInput = input("Folder to Encrypt:")
    for filename in os.listdir(folderInput):
        files = os.path.join(folderInput,filename)
        with open(files,'rb') as f:
            original_data=f.read()
        dec_Folder = fK.encrypt(original_data)
        with open(files,'wb') as dF:
            dF.write(dec_Folder)
        dF.close()
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