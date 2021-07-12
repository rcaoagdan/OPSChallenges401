#!/usr/bin/env python3

# Script: Ops Challenge 06 File Encryption
# Author: Ray Caoagdan
# Date of Last Revision: 07/112021
# Purpose: Encryption with Python


##############################################################################
# Import Library 
##############################################################################
import cryptography
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
        print("Decrpyting file")
        main_menu()
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
    with open('filekey.key','wb') as filekey:
        filekey.write(key)

##############################################################################
# loads key
##############################################################################
def loadKey():
   return open('filekey.key', 'rb').read()

##############################################################################
# File Encryption 
##############################################################################
def fileEncryption():
    #print("FILE ENCRPYTION \n")
    #filePath = input("File to Encrpyt:")
    #loadKey()
    #f = Fernet(filekey)
   # with open(filePath, "rb") as masterFile:
       # masterFile_data=masterFile.read()
    #encryptedFile = f.encrypt(masterFile_data)
    #with open(filePath,"wb") as masterFile:
       # masterFile.write(encryptedFile)
    main_menu()

##############################################################################
# File Decryption
##############################################################################
def fileDecryption():
    print("WIP")
    main_menu()

##############################################################################
# Message Encryption
##############################################################################
def msgEncryption():
    print(" ")
    print("Message Encryption")
    writeKey()
    key=loadKey()
    user_msg = input("MESSAGE TO ENCRYPT:")
    f=Fernet(key)
    msg=f.encrypt(user_msg.encode())
    print(" ")
    print("Encrpyted Message:")
    print(msg)
    main_menu()
##############################################################################
# Message Decryption
##############################################################################
def msgDecryption():
    print(" ")
    print("Message Decryption:")
    writeKey()
    key=loadKey()
    f=Fernet(key)
    udmsg = input("MESSAGE TO DECRYPT:")
    dMsg=f.decrypt(udmsg)
    print(" ")
    print("Decrypted Message:")
    print(dMsg.decode())
    main_menu()

##############################################################################
# Main
##############################################################################
main_menu()
##############################################################################
# End
##############################################################################