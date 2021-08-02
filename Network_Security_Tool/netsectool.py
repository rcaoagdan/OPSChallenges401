#!/usr/bin/env python3

# Script: Network Security Tool
# Author: Ray Caoagdan
# Date of Last Revision: 08/02/2021
# Purpose:  Scan Ports | ICMP Sweep

##############################################################################
# Import Library 
##############################################################################
import random
from re import VERBOSE
import sys
from typing import List
from ipaddress import IPv4Network
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
    print(" ")
    print("*" * 50) 
    print("TCP Scan")
    print("*" * 50) 
    print(" ")

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
    print(" ")
    print("*" * 50) 
    print("ICMP PINGSWEEP")
    print("*" * 50) 
    print(" ")
    
    
    network=input("Input IP range to ping in format 0.0.0.0/0: ")
    addresses=IPv4Network(network)
    liveCount=0

    print("*" * 50) 
    print("Pinging:" + network )
    print("Ping Sweep started at: " + str(datetime.now()))
    print("*" * 50)
    print (" ")

    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            continue
        resp= sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)

        if resp is None:
            print (str(host) + " is down/unresponsive.")
        elif(
            int(resp.getlayer(ICMP).type) == 3 and 
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
         ):
            print(str(host)  + " is blocking ICMP traffic")
        else:
            print(str(host)  + " is respoinding.")
            liveCount += 1
        
    print(liveCount/addresses.num_addresses + " hosts are online")

    print (" ")
    print("*" * 50) 
    print("Pinged:" + network )
    print("Ping Sweep ended at: " + str(datetime.now()))
    print("*" * 50)
    print (" ")
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

#### Sources/ Codes used as reference/copied #### 

##TCP##
# https://gist.github.com/mic159/c7133509af81dad409b79b8c4838f4bd

##ICPMP Ping Sweep##
# https://thepacketgeek.com/scapy/building-network-tools/part-10/


#### For your Reference ####

### TCP SCAN ###

# NULL = 0x00
# END = 0x01
# SYN = 0x02
# RST = 0x04
# PSH = 0x08
# ACK = 0x10
# SYN + ACK = 0x12
# RST + ACK = 0x14
# PSH + ACK = 0x18
### IPCMP ###

## Tpye 3 ## - Destuination Unreachable

##CODE##
# 1 - Host Unreachable
# 2 - Protocol Unreachable
# 3 - Port Unreachable
# 9 - Communication with Destination Network is Administratvely Prohibited 
# 10 - Communication with Destination Host is Administratively Prohibited
# 13 - Communication with Administrativley Prohibited 
