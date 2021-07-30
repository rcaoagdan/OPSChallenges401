#!/usr/bin/env python3

# Script: Network Security Tool
# Author: Ray Caoagdan
# Date of Last Revision: 07/29/2021
# Purpose:  Scan Ports

##############################################################################
# Import Library 
##############################################################################
import random
import sys
from typing import List
from scapy.all import *
from datetime import datetime

##############################################################################
# Main Menu
##############################################################################
def main_menu():
    print("*" * 50)
    print("What Would You Like to Do?")
    print("1.TCP Port Scanner")
    print("2.ICMP Ping Sweep")
    print("3.Exit")
    print("*" * 50)
    mainInput= input("OPTION: " ) 
    print("*" * 50 + "\n")
    if mainInput == '1':
        tcpScan()
    elif mainInput ==  '2':
        ICMPSweep()
    elif mainInput == '3':
        exit
    else:
        print("Incorrect Selection")
        main_menu

##############################################################################
# TCP Port Scanner
##############################################################################
def tcpScan():
    dIP = input("Enter a Destination IP Address:")
    nPorts = int(input("Enter number of ports you wish to scan: "))
    rPort=list(map(int,input("\nEnter Ports: ").strip().split()))[:nPorts] 
    srcPort = random.randint(1000,50000) 
    SYNACK = 0X12 # Var for SYNACK flag
    RSTACK = 0X14 # Var fpr RSTACK flag

    print("*" * 50) 
    print("Scanning:" + dIP )
    print("Scanning started at: " + str(datetime.now()))
    print("*" * 50)
    print (" ")

    for dstPort in rPort:
        resp=sr1(IP(dst=dIP)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)
    
        if resp is None:
            print("Port " + str(dstPort) + " is filtered and silently dropped")
        
        elif (resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == SYNACK):
                print("Port " + str(dstPort) + " is open")

            elif(resp.getlayer(TCP).flags == RSTACK):
                print("Port " + str(dstPort) + " is closed")

            else:
                print("ERROR TCP SCAN")

        else:
            print("ERROR SCANNING")
    print(" ")
    print("*" * 50) 
    print("Scanned:" + dIP )
    print("Scan Ended at: " + str(datetime.now()))
    print("*" * 50 + "\n") 
    main_menu()

##############################################################################
# ICMP Sweep
##############################################################################
def ICMPSweep():
    print("WIP")
    main_menu()
##############################################################################
# Main
##############################################################################
main_menu()
##############################################################################
# End
##############################################################################

##############################################################################
# Source/ Refrence
##############################################################################
# https://gist.github.com/mic159/c7133509af81dad409b79b8c4838f4bd

