import os
import sys
import time
import pythonwhois 
sys.path.append('core/')
from adminfinder import *
from geoip import *
from landiscover import *
from listener import *
from wafdetection import *
from generator import *
from ipresolver import *
from portscanner import *
from banner import *
from wifijammer import *
from payloadgen import *


try:
	from termcolor import colored, cprint

except ImportError as ie:
	cprint(str(ie), 'red')


class PlatformCheck(object):
	def OSCheck(self):
		if sys.platform == 'win32':
			cprint("[-] Windows 32-Bit Detected! Gloom Framework is Unix/Linux Based!", 'red')

		if sys.platform == 'win64':
			cprint("[-] Windows 64-Bit Detected! Gloom Framework is Unix/Linux Based!", 'red')

		else:
			cprint("[!] Unix/Linux Kernel Detected!", 'green')

checkpltf = PlatformCheck()
os.system('clear')
checkpltf.OSCheck()
time.sleep(1.5)
os.system('clear')

class checkRoot(object):
	def sudoCheck(self):
		if not os.geteuid() == 0:
			os.system('clear') 
			print("[gloom_error]" + colored(" This Script Must be Run as Root!", 'red'))
			sys.exit(0) 

checksudo = checkRoot()
checksudo.sudoCheck() 

class GloomMain(object):

	def on_load(self):
		__version__ = '1.0'
		__author__ = "Josh"
		__date__ = "August 20, 2017"
		__tools__ = "8"

		gloom_tools = [
			'admin_panel_finder',
			'web_whois',
			'ip_geolocation',
			'discover_lan_devices',
			'website_ip_resolver',
			'wifi_jammer',
			'listener',
			'waf_scanning',
			'port_scanner',
			'payload_generator'
	
			]

		gloom_prompt = raw_input("\n[" + colored('gloom', 'red') + "] ") 
		
		if gloom_prompt == 'exit':
			sys.exit(0)
       		
		if gloom_prompt == 'clear':
			os.system('clear')
			return gloom_main.on_load() 

		if gloom_prompt == 'info':
			print("Developer: " + colored(__author__, 'green'))
			print("Version: " + colored(__version__, 'green')) 
			print("Date: " + colored(__date__, 'green'))
			print("Tools: " + colored(__tools__, 'blue'))  
			return gloom_main.on_load() 
		
		if gloom_prompt == 'load':
			load_mod = gloom_prompt + ''   
			if load_mod not in gloom_tools:
				print("[gloom_error] " + colored("Failed To Load Module", 'red'))
				return gloom_main.on_load() 

			elif load_mod in gloom_tools:
				print(gloom_prompt + '(' + colored(load_mod, 'red') + ')') 

		if gloom_prompt == 'help':
			print "\n"
			print "\t\t|Core Commands|"
			print "=" * 40
			print "help :: " + colored("Show This List Again", 'blue')
			print "clear :: "+ colored("Clear Screen", 'blue')
			print "exit :: " + colored("Leaves Gloom Framework", 'blue')
			print "info :: " + colored("Shows Tool Information", 'blue')
			print "\n"
			print "\t\t|Tools|"
			print "=" * 40 
			print "admin_panel_finder :: " + colored("Find Website Admin Panels", 'blue')
			print "ip_geolocation :: " + colored("Geolocate an IP Address", 'blue')
			print "web_whois :: " + colored("Gather WHOIS Information on a Target", 'blue') 
			print "\n"
			print "discover_lan_devices :: " + colored("Detect Users/Devices on LAN", 'blue')
			print "website_ip_resolver :: " + colored("Get IP Address of Website", 'blue')
			print "payload_generator :: " + colored("Generate Windows Payload", 'blue') 
			print "\n"
			print "wifi_jammer :: " + colored("Wireless Deauthentication Attack", 'blue')
			print "listener :: " + colored("Listen For Connections on Network", 'blue')
			print "\n"
			print "waf_scanning :: " + colored("Scan for Website Firewall", 'blue')
			print "port_scanner :: " + colored("Scan for Open Ports", 'blue')
			print "\n"

			return gloom_main.on_load() 
		
		elif gloom_prompt == 'admin_panel_finder':
			findAdmin() 
			return gloom_main.on_load()

		elif gloom_prompt == 'ip_geolocation':
			geolocate() 
			return gloom_main.on_load() 
		
		elif gloom_prompt == 'discover_lan_devices':
			DiscoverLiveHosts()
			return gloom_main.on_load() 

		elif gloom_prompt == 'website_ip_resolver':
			ResolveIP()
			return gloom_main.on_load()

		elif gloom_prompt == 'web_whois':
			os.system('clear') 
			CORE_STRING = colored("[web_whois]", 'blue')
       			TARGET = raw_input(CORE_STRING + " Website> ")
			domains = [TARGET]
			for dom in domains:
				details = pythonwhois.get_whois(dom)
	        		print details['contacts']['registrant'] 

			return gloom_main.on_load() 

		elif gloom_prompt == 'wifi_jammer':
			RunScapyBasicDeauthentication()
			return gloom_main.on_load() 

		elif gloom_prompt == 'listener':
			sockListen()
			sockAccept() 
			return gloom_main.on_load() 
		
		elif gloom_prompt == 'waf_scanning':
			RunDetection()
			return gloom_main.on_load() 

		elif gloom_prompt == 'port_scanner':
			PortScanner()
			return gloom_main.on_load() 
		
		elif gloom_prompt == 'payload_generator':
			payload = EXEPayloads() 
			payload.GetInputVariables() 
			payload.Meterpreter() 
			return gloom_main.on_load() 

		else:
			print("[gloom_error] " + colored("Unknown Command/Argument!", 'red'))
			return gloom_main.on_load()  

def SecondaryBanner():
	cprint("[]    Gloom Framework        []", 'blue')
	time.sleep(0.1) 
	cprint("[]      @joshDelta           []", 'green') 
	time.sleep(0.1) 
	cprint("[]      <-Partner->          []", 'green')
	time.sleep(0.1) 
	cprint("[] http://unrealsecurity.net []", 'blue')
	time.sleep(1.5) 

if __name__ == "__main__":
	load_banner() 
	SecondaryBanner() 
	gloom_main = GloomMain()
	gloom_main.on_load() 
