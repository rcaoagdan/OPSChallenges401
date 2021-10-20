#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests

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
print("The HTTP RESONSE IS....")
print(response2)
print(" ")
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox


# Stretch Goal
# - Give Cookie Monster handss