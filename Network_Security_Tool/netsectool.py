#!/usr/bin/env python3

# Script: Network Security Tool
# Author: Ray Caoagdan
# Date of Last Revision: 
# Purpose:  Scan Ports



##############################################################################
# Import Library 
##############################################################################
import random
import sys
from scapy.all import ICMP,IP,sr1,TCP
from scapy.volatile import RandShort
from datetime import datetime

##############################################################################
# Global Variables
##############################################################################
dIP = input("Enter a Destination IP Address:") # Destination IP
nPorts = int(input("Enter number of ports you wish to scan: "))
rPort=list(map(int,input("\nEnter Ports: ").strip().split()))[:nPorts]
# mPort = input('Enter Minimum:') # set minum
# MxPort = input('Enter Maximum Port:') # set max port range
srcPort = RandShort() # Generate small random source port number from scappy 
SYNACK = 0X12
RSTACK = 0X14
##############################################################################
# Check validity of inputs
##############################################################################
#if int(mPort) >= 0 and int(MxPort) >= 0 and int(MxPort) >= int(mPort):
        # pass
       #  rPorts = range(int(mPort),int(MxPort)+1)
# else:
        # print("Invalid Range!!! \n")
        # print("Learn some math \n")
        # print("Now Exiting.....")
        # sys.exit(1)
##############################################################################
# End of Validity check
##############################################################################



##############################################################################
# TCP Port open Closed
##############################################################################
def tcpScan():
    print("*" * 50)
    print("Scanning:" + dIP )
    print("Scanning started at:" + str(datetime.now()))
    print("*" * 50)
    for dstPort in rPort:
        resp=sr1(IP(dst=dIP)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)
    
        if resp is None:
            #@print(f"{dIP}:{rPorts} is filtered and silently dropped")
            print("Port" + str(rPort) + "is filtered and silently dropped")
        
        elif (resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == SYNACK):
                #send_rst= sr1(IP(dst=dIP)/TCP(sport=srcPort,dport=dstPort,flags="R"),timeout=1,verbose=0)
                #print(f"{dIP}:{rPorts} is open")
                print("Port" + str(rPort) + " is open")

            elif(resp.getlayer(TCP).flags == RSTACK):
                print(f"{dIP}:{rPort} is closed")
            
            else:
                print("ERROR TCP SCAN")

        else:
            print("ERROR SCANNING")

##############################################################################
# Main
##############################################################################
tcpScan()
##############################################################################
# End
##############################################################################