# Ops Challenge - Attack Tools Part 2 of 3

## Demo Code




#!/usr/bin/python3

import nmap
import os,sys

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)
bport = input("Enter a staring port: ")
eport = input("Enter an ending port: ")
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3)              \n""") ### TODO: Select what your third scan type will be
print("You have selected option: ", resp + " \n")
range= (bport-eport)

### TODO: Prompt the user to type in a port range for this tool to scan

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, str(range), '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    ### TODO: Add missing code block here
    print("Please enter a valid option") 
elif resp == '3':
    ### TODO: Add missing code block here
    print("Please enter a valid option") #
elif resp >= '4':
    print("Please enter a valid option")
