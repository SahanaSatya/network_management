from scapy.all import *
import sys
from io import BytesIO
import smtplib
packets = rdpcap('R2_int_down_tD.pcap')

fromaddr = "sahanacuboulder@gmail.com"
toaddrs = 'sasa7902@colorado.edu'


import subprocess
import re
print("Device".ljust(20)+"Interface Name".ljust(20)+"Description".ljust(20)+"Operational Status".ljust(20)+"Physical Address".ljust(20)+"Admin Status".ljust(20)+"Incoming Unicast Packets Counter".ljust(20))
interfaces = ["ifName","ifAlias","ifOperStatus","ifPhysAddress","ifAdminStatus","ifInUcastPkts"]
while True:
    Name=[]
    Descr=[]
    OperStatus=[]
    PhysAddress=[]
    AdminStatus=[]
    InUcastPkts=[]
    for i in range(0,6):
        p1 = subprocess.check_output(["snmpwalk","-v1","-cpublic","198.51.100.3",interfaces[i]])
        p = re.split('[-\n]', str(p1))
        for j in p:
            if (j !="IF") and (len(j) > 1):
                k = re.split('[-:]',str(j))
                if i == 0:
                   Name.append(k[3])
                if i==1:
                   Descr.append(k[3])
                if i==2:
                   OperStatus.append(k[3])
                if i==3:
                    if len(k) > 4:
                        PhysAddress.append(str(k[3])+":"+str(k[4])+":"+str(k[5])+":"+str(k[6])+":"+str(k[7])+":"+str(k[8]))
                    else:
                        PhysAddress.append(str(k[3]))
                if i==4:
                    AdminStatus.append(k[3])
                if i==5:
                    InUcastPkts.append(k[3])
    i =0
    for name in Name:
        print("R1".ljust(20)+str(Name[i]).ljust(20)+str(Descr[i]).ljust(20)+str(OperStatus[i]).ljust(20)+str(PhysAddress[i]).ljust(20)+str(AdminStatus[i]).ljust(20)+str(InUcastPkts[i]).ljust(20))
        i += 1
    Name=[]
    Descr=[]
    OperStatus=[]
    PhysAddress=[]
    AdminStatus=[]
    InUcastPkts=[]
    for i in range(0,6):
        p1 = subprocess.check_output(["snmpwalk","-v2c","-cpublic","198.51.100.4",interfaces[i]])
        p = re.split('[-\n]', str(p1))
        for j in p:
          if (j !="IF") and (len(j) > 1):
            k = re.split('[-:]',str(j))
            if i == 0:
               Name.append(k[3])
            if i==1:
                Descr.append(k[3])
            if i==2:
                OperStatus.append(k[3])
            if i==3:
                if len(k) > 4:
                    PhysAddress.append(str(k[3])+":"+str(k[4])+":"+str(k[5])+":"+str(k[6])+":"+str(k[7])+":"+str(k[8]))
                else:
                    PhysAddress.append(str(k[3]))
            if i==4:
                AdminStatus.append(k[3])
            if i==5:
                InUcastPkts.append(k[3])
    i =0
    for name in Name:
        print("R2".ljust(20)+str(Name[i]).ljust(20)+str(Descr[i]).ljust(20)+str(OperStatus[i]).ljust(20)+str(PhysAddress[i]).ljust(20)+str(AdminStatus[i]).ljust(20)+str(InUcastPkts[i]).ljust(20))
        i += 1
    Name=[]
    Descr=[]
    OperStatus=[]
    PhysAddress=[]
    AdminStatus=[]
    InUcastPkts=[]
    for i in range(0,6):
        p1 = subprocess.check_output(["snmpwalk","-v3","-lauthNopriv","-amd5","-Anetman123","-unetman_user","198.51.100.5",interfaces[i]])
        p = re.split('[-\n]', str(p1))
        for j in p:
          if (j !="IF") and (len(j) > 1):
            k = re.split('[-:]',str(j))
            if i == 0:
                  Name.append(k[3])
            if i==1:
                Descr.append(k[3])
            if i==2:
                OperStatus.append(k[3])
            if i==3:
                if len(k) > 4:
                    PhysAddress.append(str(k[3])+":"+str(k[4])+":"+str(k[5])+":"+str(k[6])+":"+str(k[7])+":"+str(k[8]))
                else:
                    PhysAddress.append(str(k[3]))
            if i==4:
                AdminStatus.append(k[3])
            if i==5:
                InUcastPkts.append(k[3])
    i =0
    for name in Name:
        print("R3".ljust(20)+str(Name[i]).ljust(20)+str(Descr[i]).ljust(20)+str(OperStatus[i]).ljust(20)+str(PhysAddress[i]).ljust(20)+str(AdminStatus[i]).ljust(20)+str(InUcastPkts[i]).ljust(20))
        i += 1
    for packet in packets:
        if packet.haslayer(UDP):
            if packet[UDP].dport == 162 and packet[IP].dst == "198.51.100.2":
                msg=""
                old_stdout, sys.stdout = sys.stdout, BytesIO()
                try:
                    packet.show()
                    msg = sys.stdout.getvalue()
                finally:
                     sys.stdout = old_stdout
                print(msg)
                username = "sahanacuboulder@gmail.com"
                password = "bengaluru123"
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(username,password)
                server.sendmail(fromaddr, toaddrs, msg)
                server.quit()
                print("Trap send to mail : " + toaddrs)
                print("---------------------------------------------------------------")
                print("---------------------------------------------------------------")
                print("---------------------------------------------------------------")
