from netmiko import ConnectHandler
ios_r1={
	'device_type':'cisco_ios',
	'username':'lab',
	'password':'lab123',
	'ip':'192.168.1.1',
}
net_connect=ConnectHandler(**ios_r1)
print("----------Routing Table ------------")
output1=net_connect.send_command('show ip route')
print(output1)
print("-----------ARP Table --------------")
output2=net_connect.send_command('show arp')
print(output2)
print("--------A Brief Status of all the Interfaces ---------")
output3=net_connect.send_command('show ip interface brief')
print(output3)
