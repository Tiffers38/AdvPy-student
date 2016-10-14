#!usr/bin/env python


#This is the port scanner.  This makes the user have to put in the specific host to scan

import optparse
from socket import *

def conn(targetHost, targetPort):
 try:
  conn = socket(AF_INET, SOCK_STREAM)
  conn.connect((targetHost, targetPort))
  print '[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' succeeded!'
 except Exception, e:
  print '[-] Connection to ' + targetHost + ' port ' + str(targetPort) + ' failed: ' + str(e)
 finally:
  conn.close()

def main():
 parser = optparse.OptionParser("%prog -t <target host(s)> -p <target port(s)>")
 parser.add_option('-t', dest='targetHosts', type='string', help='Specify the target host(s); Separate them by commas')
 parser.add_option('-p', dest='targetPorts', type='string', help='Specify the target port(s); Separate them by commas')

 (options, args) = parser.parse_args()

 if (options.targetHosts == None) | (options.targetPorts == None):
  print parser.usage
  exit(0)

 targetHosts = str(options.targetHosts).split(',')
 targetPorts = str(options.targetPorts).split(',')

 setdefaulttimeout(5)

 for targetHost in targetHosts:
  for targetPort in targetPorts:
   conn(targetHost, int(targetPort))
   print ''

if __name__ == '__main__':
 main()
 
 
 #This utilizes the nmap function in python.  
 import optparse 
import nmap

def nmapScan(targetHosts, targetPorts):
 try:
  scanner = nmap.PortScanner()
  scanner.scan(targetHosts, targetPorts)

 for targetHost in scanner.all_hosts():
  if scanner[targetHost].state() == 'up':
   print targetHost + ' is up'
 for targetPort in scanner[targetHost]['tcp']:
  print 'Port ' + str(targetPort) + '/tcp ' + scanner[targetHost]['tcp'][int(targetPort)]['name'] + ' is ' + scanner[targetHost]['tcp'][int(targetPort)]['state']
  print ''
 except Exception, e:
  print '[-] Something bad happened during the scan: ' + str(e)

def main():
 ...

 targetHosts = str(options.targetHosts)
 targetPorts = str(options.targetPorts)

 nmapScan(targetHosts, targetPorts)
 
 
 #This additional function grab() grabs the banner of the host.  Add this to the port scanner script
 def conn(targetHost, targetPort):
 try:
  conn = socket(AF_INET, SOCK_STREAM)
  conn.connect((targetHost, targetPort))
  print '[+] Connection to ' + targetHost + ' port ' + str(targetPort) + ' succeeded!'
  grab(conn)
 ...

def grab(conn):
 try:
  conn.send('Hello, is it me you\'re looking for? \r\n')
  ret = conn.recv(1024)
  print '[+]' + str(ret)
  return
 except Exception, e:
  print '[-] Unable to grab any information: ' + str(e)
  return
  
#This function will grab the HTTP banner of the host if on port 80. Edit the conn() function

def conn(targetHost, targetPort):
 try:
  ...
  if targetPort == 80:
   grabHTTP(conn)
  else:
   grab(conn)
 ...

def grabHTTP(conn):
 try:
  conn.send('GET HTTP/1.1 \r\n')
  ret = conn.recv(1024)
  print '[+]' + str(ret)
  return
 except Exception, e:
  print '[-] Unable to grab any information: ' + str(e)
  return
  
 
