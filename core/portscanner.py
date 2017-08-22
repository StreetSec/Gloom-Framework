import os
import sys
import time
import subprocess
from termcolor import colored, cprint

'''
	Since Gloom Framework is in it's early development stage,
A more proper Port Scanner is in the works and should be released shortly.
Sorry For the Poor Notice.

'''

def PortScanner():
	try:
		CORE_STRING = colored("[port_scanner]", 'blue')
		WEBSITE = raw_input(CORE_STRING + " Website> ")
		xterm_scan = "xterm -e " + "nmap --open " + WEBSITE
		os.system(xterm_scan)
	
		cli_string = 'nmap --open ' + WEBSITE
		os.system(cli_string)

	except KeyboardInterrupt:
		cprint("\n[!] user Abort Scan!", 'red')
		sys.exit(0) 

	except:
		pass



