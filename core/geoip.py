import os
import sys
import time
import urllib2
import socket
from termcolor import colored, cprint

def geolocate():
	CORE_STRING = colored("[ip_geolocation]", 'blue')
	
	ip_addr = raw_input(CORE_STRING +  " IP Address> ")
	REVERSE_SOCKET_DNS = socket.getfqdn(ip_addr)
	geoip = urllib2.urlopen('http://api.hackertarget.com/geoip/?q='
		+ip_addr).read().rstrip()
	
	cprint("[*] Authenticating API...", 'blue')
	time.sleep(1)
	cprint("[!] Gathering Information...", 'blue')
	time.sleep(1) 
	print("\tIP Information:\n\n ")
	print geoip



