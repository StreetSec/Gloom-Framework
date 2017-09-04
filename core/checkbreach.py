import os
import requests
import sys
import time
import socket
import datetime
import json
from bs4 import BeautifulSoup
from termcolor import cprint, colored

class Breach(object):

    def RunMainCheck(self, email):
        email_list = []
        api = "https://haveibeenpwned.com/api/v2/breachedaccount/%s?truncateResponse=true" % email
        time.sleep(1)

        print "[!] Trying to Authenticate Email: " + colored('%s', 'blue') % email
        r = requests.get(api,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'})
        auth_status = 200

        if(r.status_code == auth_status):
            try:
                pwnedSites = json.loads(r.text)
                for site in pwnedSites:
                    print "[+] %s was comprimised at %s breach!" % (email, site["Name"])
                    email_list.append(email)

            except Exception:
                pass

        else:
            cprint("[!] Email Has Not Been Comprimised in a Breach", 'red')







