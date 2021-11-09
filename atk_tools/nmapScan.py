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
bport = int(input("Enter a staring port: "))
eport = int(input("Enter an ending port: "))
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) O/S Detection            \n""") 
print("You have selected option: ", resp + " \n")




if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    for port in range(bport,eport+1):
        scanner.scan(ip_addr, str(port), '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    for port in range(bport,eport+1):
        scanner.scan(ip_addr, str(port), '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Determining Target's O/S")
    target_machine = scanner.scan(ip_addr, arguments='-O')
    print(target_machine['scan'][ip_addr]['osmatch'][0]['osclass'][0]['osfamily'])
else:
    print("Please enter a valid option")
