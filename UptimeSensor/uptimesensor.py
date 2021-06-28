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

##############################################################################
# Set Variable for a user input ip address
##############################################################################
ip_input=input("Please enter in an IP Adress:")
#ping_request=os.system("ping -w 2000 " + ip_input)
ping_request=os.system("ping " + ip_input)
current_date_time=datetime.datetime.now()
invalid=current_date_time , 'Network Not Active to', ip_input
valid=current_date_time , 'Network Active to', ip_input
##############################################################################
# Ping Function
##############################################################################
def ping_function():
    if ping_request == 0:
       print(current_date_time,"Network Active to",ip_input)
    else:
      print(current_date_time,"Network NOT Active to",ip_input)

##############################################################################
# Main
##############################################################################

print(ping_request)
print(" ")
ping_function()