## Overview 
Oftentimes, security operations and general systems administration duties overlap. One such example is the need to monitor events taking place on infrastructure throughout the day. Today you will begin writing an uptime sensor tool that checks systems are responding. This can be particularly useful for tracking the status of critical infrastructure, such as web servers.

## Part 1
### Requirements
In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

The script must: 

* Transmit a single ICMP (ping) packet to a specific IP every two seconds.
* Evaluate the response as either success or failure.
* Assign success or failure to a status variable.
* For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
    Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8 

***Stretch Goals (Optional Objectives)***
In Python, add the below features to your uptime sensor tool.

The script must: 

* Save the output to a text file as a log of events.
* Accept user input for target IP address.


## Part 2
Today you will finish writing an uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.

Requirements
In Python, add the below features to your uptime sensor tool.

The script must:

* Send an email to the administrator if a host status changes from “up” to “down”.
* The email message should clearly indicate which host status changed, the status before and after, and a timestamp of the event.
* Send an email to the administrator if a host status changes from “down” to “up”.
* The email message should clearly indicate which host status changed, the status before and after, and a timestamp of the event.

### Stretch Goals (Optional Objectives)
In Python, add the below features to your uptime sensor tool.

The script must:

* Save all status changes to an event log. Each event must include a timestamp, event code, any host IP addresses involved, and a human readable description.
* Send mail from an active mail server on the host executing the Python script, instead of SMTP relay out to something like Gmail.
