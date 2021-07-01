#!/usr/bin/env python3

# Script: Ops Challenge Uptime Sensor
# Author: Ray Caoagdan
# Date of Last Revision: 06/30/2021
# Purpose: Uptime Sensor 
# Part 1: Ping Status and Print to File
# Part 2: Email Ping Status

##############################################################################
# Import Library 
##############################################################################
import os
import datetime
import getpass
import email
import smtplib # email sending 
from email.message import EmailMessage #email module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

##############################################################################
# Set Variable for a user input ip address
##############################################################################
ip_input=input("Please enter in an IP Address:")
ping_request=os.system("ping -w 2000 " + ip_input)
current_date_time=datetime.datetime.now()
dataFile=open("data.txt", "w")

##############################################################################
# Ping Status Function | Prints to results to file
##############################################################################
def PingStatus():
   for ping in range (0,4):
      if ping_request == 0: 
         print(current_date_time,"Network Active to",ip_input, file=dataFile)
        
      else:
         print(current_date_time,"Network NOT Active to",ip_input,file=dataFile)
     

##############################################################################
# Email Ping Status
##############################################################################
def mailPingStatus(): 
   adminEmail=input('Enter Administrators Email:')
   userEmail=input('Enter your Email:')
   userPass=getpass.getpass("Password:")
   mail=smtplib.SMTP_SSL("smtp.gmail.com", 465)
   files=open("data.txt", "r")
   emailMSG=MIMEMultipart()
   emailMSG['From']=userEmail
   emailMSG['To']=adminEmail
   emailMSG['Subject']='Ping Status'
   #email_body="Hello, attached are the results of the Ping Status"
   emailMSG.attach(MIMEText(files.read(), "plain"))
   files.close()
   mail.ehlo()
   mail.login(userEmail, userPass)
   mail.sendmail(userEmail, adminEmail, emailMSG.as_string())
   mail.quit()
##############################################################################
# main
##############################################################################
print(" ")
PingStatus()
mailPingStatus()
##############################################################################
# End
##############################################################################