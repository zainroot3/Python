# import os
# os is the one of tha important library to perform operations on our os
# print(os.listdir())
# os.listdor os is used to list tha directories
# os.mkdir("test.dir")
# os.mkdir is used to make folder
# os.rmdir("test.dir")
# os.rmdir() is used to remove directory
# import subprocess
# # this library allows us to run shell commands directly in python program
# result = subprocess.run(["ls", "ls -a"], capture_output=True, text=True)
# print(result.stdout)
# some more libraries
"""
os
subprocess
socket
scapy
cryptography
requests
paramiko
python-nmap(NMAP)
Pyshark
Impacket
"""
# These are the tops library in cybersecurity
import subprocess

# subprocess.run(["ls", "ls -a"], capture_output=True, text=True)
# subprocess.run executes the command on the terminal
# capture_output is used to run terminal insde python script
# like listing files in directory

# process = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE, text=True)
# Popem is used to capture real time outputs
# for line in process.stdout:
#     print(line.strip())
# you can also say it is used to run tools
# sab se pehlay import library
# variable mai store kya aur Popen kr ke command and kiss pr enter kr dya
# stdout paramteer bss yeh kr rha yeh output stdout mai le aye ga
# then ham stdout ko use kr sktay hai
# line.strip() mai strip use hota to remove anything to by dafault yeh ectra spaces hatta de ga

# important tips
# kbi bi shell=True ni rkhna
# sanitize krna imput ko
# use subporess.run over os.system
