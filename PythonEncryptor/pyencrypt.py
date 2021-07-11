#!/usr/bin/env python3

# Script: Ops Challenge 06 File Encryption
# Author: Ray Caoagdan
# Date of Last Revision: 07/112021
# Purpose: Encryption with Python


##############################################################################
# Import Library 
##############################################################################

from cryptography.fernet import Fernet 

##############################################################################
# Key Generation - Saves to a file
# Genrates key to be used to encrpy/decrpyt files
##############################################################################

key = Fernet.generate_key()
with open('filekey.key','wb') as filekey:
    filekey.write(key)

##############################################################################
# Main Menu Fuction
##############################################################################
def main_menu():
    print (" ")
    print ("What would you like to do? /n")
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
        print("Encrypting Message")
        main_menu()
    elif mainResponse == '4':
        print("Decrypting Message")
        main_menu()
    else:
        print("Incorrect selection main")
        main_menu()

##############################################################################
# Key Generation 
##############################################################################
#def writeKey():
key = Fernet.generate_key()
with open('filekey.key','wb') as filekey:
    filekey.write(key)

##############################################################################
# loads key
##############################################################################
def loadKey():
   return open('filkey.key', 'rb').read()

##############################################################################
# File Encryption 
##############################################################################
def fileEncryption():
    print("FILE ENCRPYTION \n")
    filePath = input("File to Encrpyt:")
    loadKey()
    f = Fernet(filekey)
    with open(filePath, "rb") as masterFile:
        masterFile_data=masterFile.read()
    encryptedFile = f.encrypt(masterFile_data)
    with open(filePath,"wb") as masterFile:
        masterFile.write(encryptedFile)
    #main_menu()
##############################################################################
# File Decryption
##############################################################################

##############################################################################
# Message Encryption
##############################################################################

##############################################################################
# Message Decryption
##############################################################################

##############################################################################
# Main
##############################################################################
main_menu()
##############################################################################
# End
##############################################################################