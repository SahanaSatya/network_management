# network_management

This project is about managing a network using various network management approaches, like SNMP, boto3 for AWS, NMAP, DHCP, etc. using Python scripts.

SNMP (Simple Network Management Protocol) : The routers are configured to use multiple versions of SNMP -v1, v2c, v3. The Network Management System or the SNMP server uses python scripts to monitor the operational status of different interfaces on different devices and also parse pcap files to determine if there is a trap from the SNMP agent. If a trap is found, then the server sends a mail notification to the network administrator. It also uses a bash shell script for getting to know system information like device uptime, number of interfaces, etc.

NMAP (Network Mapper) : Python scripts are used to automate the nmap function. Ping sweep is used for taking an inventory of the ip addresses in the network. A list of known IP addresses serving as web servers is maintained and any rogue device acting as a web server on the network is determined using the tcp syn from the server to the subnet broadcast.

AWS: Python module boto3 is used to manage the EC2 servers and S3 buckets deployed on AWS. Python scripts for EC2 management automate the creation, fetching info about the running instances and stopping the required instances; it also takes inventory of various details about the network, CPU and so on; it notifies the network administrator in case of excess utilization and stops those instances and spins up new ones. Python scripts for S3 management monitors the bucket for aged files and deletes those that have expired the validity period of files. 

DHCPv4config: This python script automates the client configuration of DHCP to obtainn DHCP addresses automatically from the DHCP server set up on the network.

Network Monitoring using Python Netmiko module- The scripts get the running config of network devices and saves in files. The script fetches information about Routing table, ARP table and interface statuses from the devices in the network.
