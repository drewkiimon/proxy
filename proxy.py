# Making a proxy server in Python
# I really like networks, so that's why I'm doing this
# And I like Python
# . . . Yes

import socket, sys
from thread import *

try:
	listening_port = int(raw_input("[*] Entering Port Number: "))
except:
	print "\n[*] User Requested An Interupt"
	print "[*] Application Exiting..."
	sys.exit()

max_conn = 5			# Max connection qeueues to hold
buffer_size = 4096		# Max socket buffer size

def start():	
	# Set up socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Initiate
		print "[*] Initializing Sockets ... Done"
		# Bind the sockets
		s.bind('', listening_port)
		print "[*] Sockets Binded Successfully..."
		# Start listening for incoming connections
		s.listen(max_conn)
		print ("[*] Servere Started Successfully [ %d ]\n" % (listening_port))
	except Exception, e:
		# Just in case anything fails
		print "[*] Unable To Initialize Socket"
		sys.exit(2)
	
	while 1:
		try:
			conn, addr = s.accept()
			data = conn.recv(buffer_size)
			start_new_thread(conn_string, (conn,data, addr))
		except KeyboardInterrupt:
			s.close()
			print "\n [*] Proxy Server Shutting Down ..."
			print "[*] Have A Nice Day"
			sys.exit()
	
	s.close()

start()