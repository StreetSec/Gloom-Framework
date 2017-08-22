import sys
import os
import time
import pythonwhois
from termcolor import colored, cprint

'''
This File Will Let use use Whois on websites.
'''

def findwhois():
	os.system('clear') 
	CORE_STRING = colored("[web_whois]", 'blue')
       	TARGET = raw_input(CORE_STRING + " Website> ")
	domains = [TARGET]
	for dom in domains:
		details = pythonwhois.get_whois(dom)
	        print details['contacts']['registrant'] 

