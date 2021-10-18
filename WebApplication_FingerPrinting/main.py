#!/usr/bin/evn python3

##############################################################################
# Information
##############################################################################

# Script : Ops Challenge  Web Application Fingerprinting
# Author : Ray Caoagdan
# Date of Last Revision : 10.16.21
# Purpose : Web Application Fingerpringiting | telnet , netcat , nmap

##############################################################################
# Import Libary 
##############################################################################
import sys , os
import socket


##############################################################################
# functions
##############################################################################

# def netcat():
#     ipAdd = input("Enter and IP Address: ")
#     portNum = input("Enter a Port Number: ")
#     os.system("nc" + ipAdd + portNum)
#     print(" ")

# def telnet():
#     ipAdd = input("Enter and IP Address: ")
#     portNum = input("Enter a Port Number: ")
#     os.system("telnet" + ipAdd + portNum)
#     print(" ")

# def nmap():
#     ipAdd = input("Enter and IP Address: ")
#     portNum = input("Enter a Port Number: ")
#     os.system("nmap -sV" + "-p" + portNum + ipAdd) 


##############################################################################
# main
##############################################################################
if __name__ == '__main__':
    while True:
        print ("*" * 50 )
        print ("Checking O/S is Linux ")
        print ("Please Wait......... \n")
        currentOS = sys.platform
        if(currentOS == "linux"):
            print("Linux System Detected \n")
            print(" ")
            ipAdd = input("Enter and IP Address: ")
            portNum = input("Enter a Port Number: ")
            print ("Welcome please look over the utilities below:")
            print ("1. netcat")
            print ("2. telnet")
            print ("3. nmap")
            print ("4. EXIT")
            mainOPT = input ("What Utility would you like to utlize? ")
            if(mainOPT == "1"):
                print(" ")
                os.system("nc" + ipAdd + portNum)
                print(" ")
            elif(mainOPT == "2"):
                print(" ")
                os.system("telnet" + ipAdd + portNum)
            elif(mainOPT == "3"):
                print(" ")
                os.system("nmap -Pn " + portNum + " -sV --script=banner " + ipAdd) 
            elif(mainOPT == "4"):
                print("Exiting system now.....")
                break
            else:
                print("INVALID SELECTION!! \n")

        else:
            print("Curent O/S is not suited to run current script")