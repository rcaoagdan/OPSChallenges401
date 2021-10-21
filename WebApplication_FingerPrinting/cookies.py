#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser
import os

#targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(" ")
print(cookie)
print(" ")

# - Send the cookie back to the site and receive a HTTP response
print("*" * 75)
response2 = requests.get(targetsite, cookies=cookie)
print("Returning the cookie back to " + targetsite + "\n")
print("The HTTP RESPONSE IS....")
print(response2)
print(" ")

# - Generate a .html file to capture the contents of the HTTP response
print("*" * 75)
print("Saving reponse.......")
html_file = 'httpFile.html'
file = requests.get(targetsite,cookies=cookie)
with open(html_file, 'wb') as f:
  f.write(file.content)
openClose = input ("Shall we open the file Y/N?")
if (openClose == "Y" or "y"):

  # - Open it with  default browser 
  webbrowser.open_new_tab(html_file) 

elif(openClose == "N" or "n"):
  print("COOKIE MONSTER SAYS BYE BYE!")  
  exit
else:
  print("COOKIE MONSTER SAD YOU DIDN'T ENTER A CORRECT INPUT")
  exit



# Stretch Goal
# - Give Cookie Monster handss