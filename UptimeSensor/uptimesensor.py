#!/usr/bin/env python3

# Script: Ops Challenge Uptime Sensor
# Author: Ray Caoagdan
# Date of Last Revision: 07/06/2021
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
         
   dataFile.close()     

##############################################################################
# Email Ping Status
##############################################################################
def emailPing():
   if ping_request == 0:
      mailPingStatusUP()
   else:
      mailPingStatusDown()

def mailPingStatusUP(): 
   adminEmail=input('Enter Administrators Email:')
   userEmail=input('Enter your Email:')
   userPass=getpass.getpass("Password:")
   mail=smtplib.SMTP_SSL("smtp.gmail.com", 465)
   dt=current_date_time.strftime("%m/%d/%Y %H:%M:%S")
   emailMSG=MIMEMultipart()
   emailMSG['From']=userEmail
   emailMSG['To']=adminEmail
   emailMSG['Subject']='Ping Status for ' + dt
   email_body=("Network is up")
   emailMSG.attach(MIMEText(email_body, "plain"))
   mail.ehlo()
   mail.login(userEmail, userPass)
   mail.sendmail(userEmail, adminEmail, emailMSG.as_string())
   mail.quit()

def mailPingStatusDown(): 
   adminEmail2=input('Enter Administrators Email:')
   userEmail2=input('Enter your Email:')
   userPass2=getpass.getpass("Password:")
   mail2=smtplib.SMTP_SSL("smtp.gmail.com", 465)
   dt2=current_date_time.strftime("%m/%d/%Y %H:%M:%S")
   emailMSG2=MIMEMultipart()
   emailMSG2['From']=userEmail2
   emailMSG2['To']=adminEmail2
   emailMSG2['Subject']='Ping Status for ' + dt2
   email_body2=("Network is down")
   emailMSG2.attach(MIMEText(email_body2, "plain"))
   mail2.ehlo()
   mail2.login(userEmail2, userPass2)
   mail2.sendmail(userEmail2, adminEmail2, emailMSG2.as_string())
   mail2.quit()
##############################################################################
# main
##############################################################################
print(" ")
PingStatus()
emailPing()
##############################################################################
# End
##############################################################################