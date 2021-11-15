#!/usr/bin/python3

import socket
import sys,os


hostip = input("Enter an IP to scan: ")
portno = int(input("Enter a port to scan: "))

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a stream socket | AF_INET Address Family | SOCK_STREAm TCP connection
connection = sockmod.connect_ex((hostip, portno))
timeout = 3 
sockmod.settimeout(timeout)


def portScanner(portno):
    if connection == 0:
        print("PORT IS OPEN")
    else:
        print("PORT IS CLOSED")
   

portScanner(portno)

