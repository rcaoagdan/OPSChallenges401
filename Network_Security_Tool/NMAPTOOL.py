#!/usr/bin/env python3

# Script: Network Security Tool-NMAP
# Author: Ray Caoagdan
# Date of Last Revision: 09/15/2021

##############################################################################
# Import Library
##############################################################################
import os
import nmap
from datetime import datetime
import logging
import logging.handlers as handlers 

##############################################################################
# logging
##############################################################################
# logger = logging.basicConfig(filename='nmaplogs.log', level=logging.DEBUG)
logger = handlers.TimedRotatingFileHandler(filename='nmaplogs.log', when="M", interval=1)
logger.setLevel(logging.DEBUG)


##############################################################################
# Ping and Port Scanner with Nmap
##############################################################################
def nmapTool():
    print(" ")
    print("*" * 50) 
    print("Ping and Port Scanner \n")
    print("*" * 50) 
    print(" ")

    target_IP = input("Please enter an IP to Ping: ")
    ping_IP=os.system("ping -w 2000 -c 1 " + target_IP)
    logging.info("Pining: " + str(target_IP))
    IPscan=nmap.PortScanner()
    
    if ping_IP == 0:
        print(" ")
        print("*" * 50) 
        print("Network is up")
        logging.info("Network is up")
        logging.info("Now checking for open ports")
        print("We Will Now Begin Scanning for Open Ports")
        print("*" * 50) 
        print(" ")
        bPort = int(input("Enter begining port: "))
        ePort = int(input("Enter ending port: "))
        print(" ")
        print("*" * 50) 
        print("Scaning Ports " + str(bPort) + "-" + str(ePort))
        print("*" * 50) 
        print(" ")
        for port in range(bPort,ePort+1):
            res = IPscan.scan(target_IP,str(port))
            res = res['scan'][target_IP]['tcp'][port]['state']# target results in dictionary
            print(f'port {port} is {res}')
            logging.info('Results of port scan is: ' +str(port)+ " " +str(res))
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
        logging.error('Error, Network not active or invalid IP Address')
        print("Network is not Active")
        print("Ping Ended at: " + str(datetime.now()))
        print("*" * 50 + "\n")  

    newScan()
    
def newScan():
    continueScan=input("Do you want to do another scan Y/N? ")

    if continueScan == "Y" or continueScan == "y":
        nmapTool()
    elif continueScan == "N" or continueScan == "n":
        exit
    else:
        print("Incorrect Selection.... Please make a correct selection \n")
        newScan()

nmapTool()

##############################################################################
# Source
##############################################################################
# geeksforgeeks.org/port-scanner-using-python-nmap/