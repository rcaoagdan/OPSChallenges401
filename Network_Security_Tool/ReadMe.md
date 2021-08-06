## Overview
Tools like Nmap are quite useful on their own, but what about customizing its capabilities? Because we know a little Python, we can explore creating our own network scanning tool with the Python library Scapy. Today you’ll begin development of your own network scanning tool.

### ***netsectool***
### Part 1: 
In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

* Utilize the scapy library
* Define host IP
* Define port range or specific set of ports to scan
* Test each port in the specified range using a for loop
    * If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
    * If flag 0x14 received, notify user the port is closed.
    * If no flag is received, notify the user the port is filtered and silently dropped.

### Part 2:
* User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
* ICMP Ping Sweep tool
    * Prompt user for network address including CIDR block, for example “10.10.0.0/24”
        Careful not to populate the host bits!
    * Create a list of all addresses in the given network
    * Ping all addresses on the given network except for network address and broadcast address
        * If no response, inform the user that the host is down or unresponsive.
        * If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
        * Otherwise, inform the user that the host is responding.
    * Count how many hosts are online and inform the user.
## Stretch Goals
* Utilize the random library
* Randomize the TCP source port in hopes of obfusticating the source of the scan
* Instead of targeting a single IP address, allow the user to specify a range of IPs and have the tool scan each one in succession.

### ***NMAPTOOL***
Utilizing nmap to: 
* Ping an IP address determined by the user.
* If the host exists, scan its ports and determine if any are open.


