import os
from time import sleep
import pexpect
from pexpect import pxssh
import socket
#from deploy_ovf import getMachineIp
import subprocess

ip_addr = subprocess.Popen("ls -lrt", stdout=subprocess.PIPE,shell=True)
(output, err) = ip_addr.communicate()
print output

test_1 = subprocess.Popen("pwd;whoami", stdout=subprocess.PIPE, shell=True)