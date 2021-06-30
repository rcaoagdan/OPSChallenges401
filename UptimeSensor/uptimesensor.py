#!/usr/bin/env python3

#Script: Ops Challenge Uptime Sensor
#Author: Ray Caoagdan
#Date of Last Revision: 06/27/2021
#Purpose: Uptime Sensor 

##############################################################################
# Import Library 
##############################################################################
import os
import datetime
import subprocess

##############################################################################
# Set Variable for a user input ip address
##############################################################################
ip_input=input("Please enter in an IP Address:")
ping_request=os.system("ping -w 2000 " + ip_input)
current_date_time=datetime.datetime.now()
print (" ")

##############################################################################
# For loop  to print network status for every ICMP transmission sent
##############################################################################
for ping in range (1,5):
   if ping_request == 0: 
      print(current_date_time,"Network Active to",ip_input) 
   else:
      print(current_date_time,"Network NOT Active to",ip_input)




