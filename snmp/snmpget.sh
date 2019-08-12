#!/bin/bash
j=(Contact Name Location Number )
count=0
echo "The Information for R1 is:"
for i in .1.3.6.1.2.1.1.4.0 .1.3.6.1.2.1.1.5.0 .1.3.6.1.2.1.1.6.0 .1.3.6.1.2.1.2.1.0
do
    echo ${j[$count]} ":" $(snmpget -v 1 -c public 198.51.100.3 $i|awk '{print $4 $5}')
    count=$((count+1))
done
echo "Uptime:" $(snmpget -v 1 -c public 198.51.100.3 .1.3.6.1.2.1.1.3.0|awk '{print $5 $6 $7}')
echo""
count=0
echo "The Information for R2 is:"
for i in .1.3.6.1.2.1.1.4.0 .1.3.6.1.2.1.1.5.0 .1.3.6.1.2.1.1.6.0 .1.3.6.1.2.1.2.1.0
do
    echo ${j[$count]} ":" $(snmpget -v 2c -c public 198.51.100.4 $i|awk '{print $4 $5}')
    count=$((count+1))
done
echo "Uptime:" $(snmpget -v 2c -c public 198.51.100.4 .1.3.6.1.2.1.1.3.0|awk '{print $5 $6 $7}')
count=0
echo""
echo "The Information for R3 is:"
for i in .1.3.6.1.2.1.1.4.0 .1.3.6.1.2.1.1.5.0 .1.3.6.1.2.1.1.6.0 .1.3.6.1.2.1.2.1.0
do
    echo ${j[$count]} ":"  $(snmpget -v 3 -l authNopriv -u netman_user -a md5 -A netman123 198.51.100.5 $i|awk '{print $4 $5}')
    count=$((count+1))
done
echo "Uptime:" $(snmpget -v 3 -l authNopriv -u netman_user -a md5 -A netman123 198.51.100.5 .1.3.6.1.2.1.1.3.0|awk '{print $5 $6 $7}')