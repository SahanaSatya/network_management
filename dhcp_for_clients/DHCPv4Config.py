from netmiko import ConnectHandler
ios_r2={
    'device_type':'cisco_ios',
    'username':'lab',
    'password':'lab123',
    'secret':'lab123',
    'ip':'198.51.100.3',
}
ios_r3={
    'device_type':'cisco_ios',
    'username':'lab',
    'password':'lab123',
    'secret':'lab123',
    'ip':'198.51.100.4',
}
ios_r4={
     'device_type':'cisco_ios',
     'username':'lab',
     'password':'lab123',
     'secret':'lab123',
     'ip':'198.51.100.5',
}
ios_list = [ios_r2, ios_r3, ios_r4 ]
configuration_set = ['int f0/0','ip addr dhcp','no sh']
for i in ios_list:
    net_connect=ConnectHandler(**i)
    net_connect.enable()
    output=net_connect.send_config_set(configuration_set)
    print(output)