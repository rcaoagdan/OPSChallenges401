#!/usr/bin/env python3

# Script: Network Security Tool
# Author: Ray Caoagdan
# Date of Last Revision: 08/04/2021
# Purpose:  Scan Ports | ICMP Sweep | Combined 

##############################################################################
# Import Library 
##############################################################################
from re import VERBOSE
from typing import List
import os
from uuid import NAMESPACE_OID
import nmap
from ipaddress import IPv4Network
from scapy.all import *
from datetime import datetime

from scapy.modules.six import u


##############################################################################
# Ping and Port Scanner with Nmap
##############################################################################

print(" ")
print("*" * 50) 
print("Ping and Port Scanner \n")
print("*" * 50) 
print(" ")

target_IP = input("Please enter an IP to Ping: ")
ping_IP=os.system("ping -w 2000 -c 1 " + target_IP)
IPscan=nmap.PortScanner()

print(" ")
print("*" * 50) 
print("Network is up")
print("We Will Now Begin Scaning for Open Ports")
print("*" * 50) 
print(" ")

if ping_IP == 0:
   
    bPort = int(input("Enter begining port: "))
    ePort = int(input("Enter ending port: "))
    print(" ")
    print("*" * 50) 
    print("Scaning Ports " + str(bPort) + "-" + str(ePort))
    print("*" * 50) 
    print(" ")
    for i in range(bPort,ePort+1):
        res = IPscan.scan(target_IP,str(i))
        res = res['scan'][target_IP]['tcp'][i]['state']# target results in dictionary
        print(f'port {i} is {res}')
    print(" ")
    print("*" * 50) 
    print("Pinged:" + target_IP )
    print("Ports Scan " + str(bPort) + "-" + str(ePort))
    print("Ping and Scan Ended at: " + str(datetime.now()))
    print("*" * 50 + "\n")  

else:
    print(" ")
    print("*" * 50) 
    print("Pinged:" + target_IP )
    print("Network is not Active")
    print("Ping Ended at: " + str(datetime.now()))
    print("*" * 50 + "\n")  



##############################################################################
# Original Code
##############################################################################
#
# Below is the Original Code for parts 1 and 2. 
# Part 3 combined parts 1 and 2 into one code. 
#
#
#
##############################################################################
# Main Menu
##############################################################################
# def main_menu():
#     print("*" * 50)
#     print("What Would You Like to Do?")
#     print("1.TCP Port Scanner")
#     print("2.ICMP Ping Sweep")
#     print("3.Exit)
#     print("*" * 50)
#     mainInput= input("OPTION: " ) 
#     print("*" * 50 + "\n")
#     if mainInput == '1':
#         tcpScan()
#     elif mainInput ==  '2':
#         ICMPSweep()
#     elif mainInput == '3':
#         exit
#     else:
#         print("Incorrect Selection")
#         main_menu




##############################################################################
# TCP Port Scanner
##############################################################################
# def tcpScan():
#     print(" ")
#     print("*" * 50) 
#     print("TCP Port Scanner \n")
#     print("*" * 50) 
#     print(" ")

#     dIP = input("Enter a Destination IP Address:")
#     nPorts = int(input("Enter number of ports you wish to scan: "))
#     rPort=list(map(int,input("\nEnter Ports: ").strip().split()))[:nPorts] 
#     srcPort = random.randint(1000,50000) 
#     SYNACK = 0X12 # Var for SYNACK flag
#     RSTACK = 0X14 # Var fpr RSTACK flag

#     print("*" * 50) 
#     print("Scanning:" + dIP )
#     print("Scanning started at: " + str(datetime.now()))
#     print("*" * 50)
#     print (" ")

#     for dstPort in rPort:
#         resp=sr1(IP(dst=dIP)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)
    
#         if resp is None:
#             print("Port " + str(dstPort) + " is filtered and silently dropped")
        
#         elif (resp.haslayer(TCP)):
#             if(resp.getlayer(TCP).flags == SYNACK):
#                 print("Port " + str(dstPort) + " is open")

#             elif(resp.getlayer(TCP).flags == RSTACK):
#                 print("Port " + str(dstPort) + " is closed")

#             else:
#                 print("ERROR TCP SCAN")

#         else:
#             print("ERROR SCANNING")
#     print(" ")
#     print("*" * 50) 
#     print("Scanned:" + dIP )
#     print("Scan Ended at: " + str(datetime.now()))
#     print("*" * 50 + "\n") 
#     main_menu()

##############################################################################
# ICMP Sweep
##############################################################################
# def ICMPSweep():
#     print(" ")
#     print("*" * 50) 
#     print("ICMP PING SWEEP")
#     print("*" * 50) 
#     print(" ")
    
    
#     netIP=input("Input IP range to ping in format 0.0.0.0/0: ")
#     netAddresses=IPv4Network(netIP)
#     liveCount=0

#     print("*" * 50) 
#     print("Pinging:" + netIP )
#     print("Ping Sweep started at: " + str(datetime.now()))
#     print("*" * 50)
#     print (" ")

#     for host in netAddresses:
#         if (host in (netAddresses.network_address, netAddresses.broadcast_address)):
#             continue
#         resp= sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)

#         if resp is None:
#             print (str(host) + " is down/unresponsive.")
#         elif(int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
#             print(str(host)  + " is blocking ICMP traffic")
#         else:
#             print(str(host)  + " is responding.")
#             liveCount += 1
        
#     print(liveCount/netAddresses.num_addresses + " hosts are online")

#     print (" ")
#     print("*" * 50) 
#     print("Pinged:" + netIP )
#     print("Ping Sweep ended at: " + str(datetime.now()))
#     print("*" * 50)
#     print (" ")
#     main_menu()


##############################################################################
# Main
##############################################################################
#main_menu()

##############################################################################
# End of Original
##############################################################################

##############################################################################
# Source/ Refrence
##############################################################################

#### Sources/ Codes used as reference/copied #### 

##TCP##
# https://gist.github.com/mic159/c7133509af81dad409b79b8c4838f4bd


##ICPMP Ping Sweep##
# https://thepacketgeek.com/scapy/building-network-tools/part-10/

## NMAP ##
# 
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

## Type 3 ## - Destination Unreachable

##CODE##
# 1 - Host Unreachable
# 2 - Protocol Unreachable
# 3 - Port Unreachable
# 9 - Communication with Destination Network is Administratvely Prohibited 
# 10 - Communication with Destination Host is Administratively Prohibited
# 13 - Communication with Administrativley Prohibited 

##############################################################################
# End
##############################################################################