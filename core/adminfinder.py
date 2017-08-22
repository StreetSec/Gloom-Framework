import os
import sys
import time

from urllib2 import urlopen, Request, URLError, HTTPError
from termcolor import colored, cprint

def findAdmin():
	CORE_STRING = colored("[admin_panel_finder]", 'blue') 
	file_var = open("link.txt", 'r')
	os.system('clear')

	TARGET = raw_input(CORE_STRING + " Website> ")
	cprint("\t\n[*] Availible Panels: \n\n", 'blue')

	while True:
		side_core_link = file_var.readline()
		if not side_core_link:
			break

		REQUEST_LINK = "http://"+TARGET+"/"+side_core_link
		REQUEST = Request(REQUEST_LINK)

		try:
			response = urlopen(REQUEST)

		except HTTPError as e:
			continue

		except URLError as w:
			continue

		except KeyboardInterrupt:
			cprint("\t\n[-] User Aborted Process!", 'red')
			sys.exit(0)

		else:
			cprint("\t[+] Success => " + REQUEST_LINK, 'green')	

 
