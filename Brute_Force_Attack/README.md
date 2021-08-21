## Overview
To properly defend against the techniques used by modern threat actors, we need to have an idea of the tools they will be using against us in an effort to circumvent our defenses. A brute force attack is a type of computer hack that relies on guessing possible combinations of a targeted password until the correct password is discovered. Sometimes brute force attacks will be augmented with word lists to create what is known as a dictionary attack, a much more efficient approach that preys upon the human tendency to use easy or familiar passwords.

Today you will begin to develop a custom tool that performs brute force attacks to better understand the types of automation employed by adversaries.

## Resources
* Iterate over a set in Python
* RockYou Password List

__Note: The RockYou passwords come bundled with Kali Linux, but you can also download them separately at the above link.__

## Requirements

### Part 1:
In Python, create a script that:

* **Mode 1: Offensive; Dictionary Iterator**

* Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
* Add a delay between words.
* Print to the screen the value of the variable.

* **Mode 2: Defensive; Password Recognized**

* Accepts a user input string.
* Accepts a user input word list file path.
* Search the word list for the user input string.
* Print to the screen whether the string appeared in the word list.

## Stretch Goals (Optional Objectives)
Pursue these optional objectives if you are an advanced user or have remaining lab time.

Most of us have probably battled a password complexity requirement at some point in recent memory. Let’s see how the logic behind that might take shape in Python. Add a third mode that achieves the below:

* **Mode 3: Defensive; Password Complexity**

* Accepts a user input string.
* Evaluates the user input string for password complexity. Impose a requirement in your code for the below metrics:
    * Were at least [qty] characters used (password length)?
    * Were at least [qty] capital letter used?
    * Were at least [qty] numbers used?
    * Were at least [qty] symbols used?
* Prints to the screen which of the above dimensions were satisfied by the user input password.
    * If all dimensions are satisfied, print a clear SUCCESS indicator for the user.

### Part 2:
Add to your Python brute force tool the capability to:

Authenticate to an SSH server by its IP address.
Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

__Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.__

### Part 3:
First, setup your target ZIP file.
* Create a .txt file containing a secret message.
* Follow the guide, How to Protect Zip file with Password, to archive the .txt file with password protection.

Next, add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.

* Use the zipfile library.
* Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.
