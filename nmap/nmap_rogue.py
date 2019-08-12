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
netman@netman:~$ cat nmap_rogue.py 
import subprocess
import re
import sys
non_rogue_IP = ['0.0.0.1','0.0.0.2','0.0.0.3','0.0.0.4','0.0.0.5','0.0.0.6','0.0.0.7','0.0.0.8','0.0.0.9','0.0.0.10']
p1 = subprocess.check_output(["sudo","nmap","-sS","-p80,443,8080","-o","file.txt","192.168.0.0/24"])
fh = open("file.txt")
with open("rogue_ip_addr.txt",'w') as fw: 
    i=0
    j=0
    li=[]
    for line in fh:
        if i != 0 and re.search("done",str(line)) == None:
            if j == 0:
                li.append(re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',line))
            if j == 3 or j ==4 or j ==5:
                state = re.findall(r'\w+',line)
                li.append(state[2])
            j +=1
            if j == 7:
                if (re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.','0.0.0.',li[0][0])) not in non_rogue_IP:
                       if li[1] == 'open' or li[2]=='open' or li[3] == 'open':
                            fw.write(li[0][0]+"\n")
                j=0
                li=[]
        i += 1
fw.close()
fh.close()
fr = open("rogue_ip_addr.txt")
for line in fr:
    print(line)
fr.close()