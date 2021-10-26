#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

MESSAGE = "Hello, you crazy rocking horse!"

def read_eof() :
	buf = ""
	try :
		while True :
			line = input("> ")
			if buf == "" : buf = line
			else : buf += "\n" + line
	except EOFError:
		return buf

if __name__ == "__main__" :
	port = 8901
	dest = sys.argv[1]
	if len(sys.argv) > 2 :
		port = int(sys.argv[2])
	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	msg = MESSAGE.encode("UTF-8")
	sock.sendto(msg, (dest, port))
	(reply, addr) = sock.recvfrom(2048)
	if reply == msg :
		print("Received correct echo")
	else :
		print("Received wrong message: %s from %s" % (reply, addr))
		sys.exit(1)
