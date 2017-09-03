import os
import sys
import socket
import time
from termcolor import colored, cprint


class Fuzzer(object):

    def TCPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[tcp_fuzzer]", 'blue')
        host = raw_input(CORE_STRING + " Host> ")
        buffer_ = 'x41' * 2048

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 443))
                s.settimeout(2)

                print "[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue')
                s.send("USER: "+buffer_+"\r\n")
                time.sleep(2)

                buffer_ = buffer_ + 'x41' * 2048

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] User Aborted Fuzz!", 'red')
                sys.exit()

            except:
                continue

    def FTPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[ftp_fuzzer]", 'blue')
        host = raw_input(CORE_STRING + " Host> ")
        buffer_ = 'x41' * 2048

        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 21))
                s.settimeout(2)

                print "[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue')
                s.send("USER: "+buffer_+"\r\n")
                time.sleep(2)

                buffer_ = buffer_ + 'x41' * 2048

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] User Aborted Fuzz!", 'red')
                sys.exit()

            except:
                continue

    def HTTPFuzzer(self):
        os.system('clear')
        CORE_STRING = colored("[http_fuzzer]", 'blue')
        host = raw_input(CORE_STRING + " Host> ")
        buffer_ = 'x41' * 2048

        HTTP_BASE_SIZE_ = 3333
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, 80))
                s.settimeout(2)

                print "[!] Sending Buffer Size of: " + colored(str(len(buffer_)), 'blue')
                s.send("USER: "+buffer_+"\r\n")
                s.send("\tGET /" + str(HTTP_BASE_SIZE_) + " HTTP/1.1\r\n")
                s.send("\tHOST: " + host + "\r\n\r\n");
                time.sleep(2)

                buffer_ = buffer_ + 'x41' * 2048

            except socket.error as wn:
                cprint("[+] Service Crashed With Buffer Size Of: " + str(len(buffer_)), 'green')
                break

            except KeyboardInterrupt:
                cprint("[-] User Aborted Fuzz!", 'red')
                sys.exit()

            except:
                continue





