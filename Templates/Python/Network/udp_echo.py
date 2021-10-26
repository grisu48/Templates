#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

BINDADDR = "0.0.0.0"
PORT = 8901

if __name__ == "__main__" :
	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	sock.bind((BINDADDR, PORT))
	print("udp echo server listening on %s:%d" % (BINDADDR, PORT))
	while True :
		msg, addr = sock.recvfrom(2048)
		print("Received %d bytes from %s" % (len(msg), addr))
		sock.sendto(msg, addr)
