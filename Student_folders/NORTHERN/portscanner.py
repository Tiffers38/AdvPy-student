#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


#Clear the screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer =raw_input("Enter a remote host to scan:")
remoteServerIP =socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print "_"*60
print "Please wait, scanning remote host", remoteServerIP
print "-"*60

#Check what time the scan started
t1 = datetime.now()

#Using the range function to specify ports (here is will scan all ports between 1 and 1024)

#We also put in some error handling for catching errors

try:
    for port in range(1,1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        print "Port{}:  Open".format(port)
    sock.close()
    
except KeyboardInterrupt:
    print"You pressed Ctrl+C"
    sys.exit()
    
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting"
    sys.exit()
    
except socket.error:
    print "Could not connect to server"
    sys.exit()
    
#Checking the time again
t2 = datetime.now()

#Calculates the difference of time, to see how long it took to run the script
total = t2-t1

#Printing the information to screen
print 'Scanning Completed in:', total

