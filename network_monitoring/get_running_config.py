from netmiko import ConnectHandler
ios_r1={
	'device_type':'cisco_ios',
	'username':'lab',
	'password':'lab123',
	'ip':'192.168.1.1',
}
ios_r2={
	'device_type':'cisco_ios',
	'username':'lab',
	'password':'lab123',
	'ip':'192.168.1.3',
}
net_connect_r1=ConnectHandler(**ios_r1)
net_connect_r2=ConnectHandler(**ios_r2)
output1=net_connect_r1.send_command('show running-config')
fh1=open('R1.txt','w')
fh1.write(str(output1))
fh1.close()
print('The running configuration of R1 is saved in R1.txt')
output2=net_connect_r2.send_command('show running-config')
fh2=open('R2.txt','w')
fh2.write(str(output2))
fh2.close()
print('The running configuration of R2 is saved in R2.txt')
