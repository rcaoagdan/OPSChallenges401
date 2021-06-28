##Overview
Oftentimes, security operations and general systems administration duties overlap. One such example is the need to monitor events taking place on infrastructure throughout the day. Today you will begin writing an uptime sensor tool that checks systems are responding. This can be particularly useful for tracking the status of critical infrastructure, such as web servers.

##Requirements
In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

The script must:

Transmit a single ICMP (ping) packet to a specific IP every two seconds.
Evaluate the response as either success or failure.
Assign success or failure to a status variable.
For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

###Stretch Goals (Optional Objectives)
In Python, add the below features to your uptime sensor tool.

The script must:

Save the output to a text file as a log of events.
Accept user input for target IP address.