# Overview

Banner grabbing, also known as “service fingerprinting,” is a way to check if your target computer supports specific services. This is useful when gathering intelligence on a target such as a web server.

***When a computer network service is activated by another program on a computer, it transmits a message. This message is traditionally known as a “banner.” By deliberately exploiting this behavior, a person can solicit service requests from specific port numbers to glean information about whether the target computer is hosting a service on the port. This is “banner grabbing.”***

## Requirements
* Prompts the user to type a URL or IP address.
* Prompts the user to type a port number.
* Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
* Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
* Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
