#!/usr/bin/python

import paramiko
import time as t

ip = '192.168.1.254'

username='Admin'
password='cisco'

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip,username=username,password=password, look_for_keys=False,allow_agent=False)

print "SSH session established %s" %ip

remote_conn=remote_conn_pre.invoke_shell()
output=remote_conn.recv(1000) # Clear Output
print output

remote_conn.send("show ip int brief\n")
t.sleep(2)
remote_conn.send("sh ver | i image\n")
remote_conn.send("sh ver | i uptime\n")
t.sleep(2)

output=remote_conn.recv(5000)
print output
