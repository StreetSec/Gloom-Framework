import os
import sys
import time
import mechanize
from termcolor import colored, cprint

class AnonEmail:

    def __init__(self):
        self.CORE_STRING = colored("[anon_email]", 'blue')
        self.INFO_STRING = colored("[anon_email]", 'green')
        self.browser = mechanize.Browser()

        self.TARGET = raw_input(self.CORE_STRING + " Recipient's Email> ")
        self.SUBJECT = raw_input(self.CORE_STRING + " Subject> ")
        self.MESSAGE = raw_input(self.CORE_STRING + " Message> ")

    def SendAnonEmail(self):

        for x in range(1):
            if self.TARGET == '' or None:
                cprint("[!] Enter Valid Input", 'red')
                break
            else:
                pass

        print self.CORE_STRING + " [!] Writing..."
        time.sleep(0.66)
        api = "http://anonymouse.org/anonemail.html"
        headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
        self.browser.addheaders = [('User-agent', headers)]

        self.browser.open(api)
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_gzip(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        self.browser.set_debug_http(False)
        self.browser.set_debug_redirects(False)
        self.browser.select_form(nr=0)

        self.browser.form['to'] = self.TARGET
        self.browser.form['subject'] = self.SUBJECT
        self.browser.form['text'] = self.MESSAGE

        try:
            result = self.browser.submit()
            response = self.browser.response().read()

        except mechanize.HTTPDefaultErrorHandler as ix:
            print self.CORE_STRING + colored(ix, 'red')

        except:
            pass

        main_repo = "The e-mail has been sent anonymously!"

        if "The e-mail has been sent anonymously!" in response or main_repo in response:
            print "\n" + self.INFO_STRING + " The email has been sent successfully."
            print self.INFO_STRING +  " Mail Should be Recieved Shortly."

        else:
            print self.CORE_STRING + " Failed to send email!"


