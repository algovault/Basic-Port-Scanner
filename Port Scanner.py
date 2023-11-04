import os
import socket
import threading
import subprocess

hostname = input("What IP Address would you like to scan?: ")
response = subprocess.call(['ping', '-c', '1', hostname])

if response == 0:
    print(hostname + " is up!")
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.000001)

        result = s.connect_ex((hostname, port))
        if result ==0:
            print("Port {} is open".format(port))
            s.close()
else: 
    print(hostname + " is down!")