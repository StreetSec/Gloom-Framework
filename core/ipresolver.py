import os
import sys
import socket
import time
from termcolor import colored, cprint

def ResolveIP():
	CORE_STRING = colored("[ip_resolver]", 'blue')
	TARGET = raw_input(CORE_STRING + " Website> ")

	try:
		ADDRESS = socket.gethostbyname(TARGET)

	except socket.gaierror as sock_error:
		cprint(str(sock_error), 'red') 

	time.sleep(1)
	print "\n[*] IP Address> " + colored(ADDRESS, 'green')


