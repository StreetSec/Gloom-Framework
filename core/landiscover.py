import os
import sys
import socket
import time
from scapy.all import *
from termcolor import colored, cprint

def DiscoverLiveHosts():
	os.system('clear')
        CORE_STRING = colored("[discover_lan_hosts]", 'blue')	
	s = socket.socket(socket.AF_PACKET, socket.SOCK_DGRAM) 
	FORMAT_STRING = colored('\n\t<IP ADDRESS>\t\t  <MAC ADDRESS>', 'cyan') 
	live_hosts = []
	NET_ID = str(raw_input(CORE_STRING + " NET ID(EXAMPLE -> 192.168.0.*)> "))
	
	ENTER_ON_PRESS = ''
	if NET_ID == ENTER_ON_PRESS or NET_ID == None:
		cprint('[~] Please Enter Valid Input!', 'red')
		return DiscoverLiveHosts()

	else:
		try:
			TOP_VERBOSE_DEBUG = False
			cprint('\t[*] Starting Scan...', 'yellow')
			time.sleep(0.5) 

			ARP_AS_1, UNANS = arping(NET_ID, verbose=TOP_VERBOSE_DEBUG)
			cprint('\t[!] Gathering Results...', 'green')
			time.sleep(1)
		
			cprint('\n\t[#] Live Hosts...') 
			print FORMAT_STRING
			
			for x in ARP_AS_1:
				print '\t' + x[0].pdst + '\t\t'+ x[1].src
				if x[1] not in live_hosts:
					live_hosts.append(x[0].pdst)
			print "\n" + CORE_STRING + " %s hosts up...."%len(live_hosts)

		except socket.gaierror as w:
			cprint('\t' + str(w), 'red')
			time.sleep(5) 
			cprint('\n\t[!] Returning...')
			return DiscoverLiveHosts() 

		except KeyboardInterrupt:
			cprint("\n\t[-] User Aborted!", 'red')
			sys.exit(0) 

		except:
			pass

 

