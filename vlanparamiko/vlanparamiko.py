# -*- coding: utf-8 -*-
"""vlanparamiko.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wOgnVHmlGbzL3jsE8KsiaC87b4eMM_I7
"""

import paramiko
import time
import sys

ip_address = "192.168.122.33"
username = "pythonauto"
password = "python123"
try:
    ssh_Client = paramiko.SSHClient()
    ssh_Client.load_system_host_keys()
    ssh_Client.set_missing_host_key_policy(paramiko.AutoAddpolicy())
    ssh_Client.connect(hostname=ip_address, username=username, password=password)
except:
    print("connection fail\n")
    sys.exit()

print("ssh connection successfull shell on the device\n")

connectto = ssh_Client.invokeshell()

connectto.send("configure terminal\n")

for n in range(2, 7):
    connectto.send("vlan" + str(n) + "\n")
    connectto.send("name python_vlan" + str(n) + "\n")
    print("python_vlan" + str(n) + "is created")
    time.sleep(0.25)

connectto.send("show vlan bri")
time.sleep(4)
connectto.send("end\n")

time.sleep(1)
console_output = connectto.recv(65535)
print(console_output)

file = open("pythonvlanscriptOutput.txt", "w+")
output = connectto.readlines()
file.write(''.join(output))
file.close()

ssh_Client.close()