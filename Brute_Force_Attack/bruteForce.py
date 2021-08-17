#!/usr/bin/env python3

# Script: Brute Force Tool
# Author: Ray Caoagdan
# Date of Last Revision: 08/16/2021

##############################################################################
# Import Library
##############################################################################
import getpass
import time
import itertools


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

##############################################################################
# Main
##############################################################################
if __name__ == '__main__':
    while True:
        print("Brute Force Attack Menu \n")
        print("1: Offensive- Dictionary Iterator")
        print("2: Defensive- Password Recognized")
        print("3: Exit")
        mode=input("Please make a selection: ")

        if(mode == "1"):
            runIterator()
        elif(mode == "2"):
            runCheckPass()
        elif(mode == "3"):
            break
        else:
            print("INVALID SELECTION \n")
##############################################################################
# End
##############################################################################