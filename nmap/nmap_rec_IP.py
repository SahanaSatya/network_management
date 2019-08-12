import subprocess
import re
import sys
p1 = subprocess.check_output(["sudo","nmap","-sP","-o","file.txt","192.168.0.0/24"])
fh = open("file.txt")
with open("ip_addr.txt",'w') as fw: 
    i=0
    for line in fh:
        if i%2 != 0 and re.search("done",str(line)) == None:
            ipaddr = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',line)
            fw.write(ipaddr[0]+"\n")
        i += 1
fw.close()
fh.close()

fr = open("ip_addr.txt")
for line in fr:
    print(line)
fr.close()
