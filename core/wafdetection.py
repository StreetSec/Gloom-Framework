import os
import sys
import time
from urllib2 import Request, urlopen, URLError, HTTPError
from termcolor import colored, cprint

def RunDetection():
		CORE_STRING = colored('[waf_detection]', 'blue') 
		try:
			link = raw_input(CORE_STRING + " Website> ")
			waf = 0
			WAF_REQ_LINK = "http://"+link
			WAF_REQ = Request(WAF_REQ_LINK)
			f  = urlopen(WAF_REQ_LINK)
			waf_response = f.read() 
			if waf_response is HTTPError or 'cloudfare' in waf_response:
				print colored("[+]", "green", attrs=['bold']) + "Cloud_Flare .. [" + colored("Detected", "green", attrs=['bold']) + "]"
				waf = True
				waf += 1

			else:
				print colored("[-]", "green", attrs=['bold']) + "Cloud_Flare .. [" + colored("None", "red", attrs=['bold']) + "]"
				waf = False
				waf -= 1

			if "Just a moment..." in waf_response or "wait" in waf_response or "Please" in waf_response or "please" in waf_response:
				print colored("[+]", "green", attrs=['bold']) + "Bot_Protection .. [" + colored("Detected", "green", attrs=['bold']) + "]"
				waf = True
				waf += 1

			else:
				print colored("[-]", "green", attrs=['bold']) + "Bot_Protection .. [" + colored("None", "red", attrs=['bold']) + "]"
				waf -= 1
				waf = False

		except KeyboardInterrupt:
			cprint("\n\t[!] User Aborted Scan! ", 'red')
			sys.exit(0)
		
		except URLError as g:
			print(CORE_STRING + colored(str(g), 'red')) 

		except HTTPError as w:
			print(CORE_STRING + colored(str(w), 'red')) 

		except:
			pass

		'''
		Lets Run some other checks for basic information
		
		'''
		response = urlopen(WAF_REQ_LINK)
		url = response.geturl() 
		print "\n"
		print "-" * 40
		print "RESPONSE: " + colored(response, 'blue') 
		print "URL: " + colored(url, 'blue')

		headers = response.info()
		print 'DATE: ' + colored(headers['date'], 'blue')
		print 'HEADERS: \n'
		print colored(headers, 'blue')
		print "\n%s Headers" %len(headers)
		
		data = response.read()
	    	print 'LENGTH  :', len(data)
	        print '-' * 40
		

