import socket

def Main():
	print 'Client is running...'
	host = "127.0.0.1"
#	host = '192.168.42.1'
	port = 5001

	s = socket.socket()
	s.connect((host, port))

	message = raw_input("-> ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print'Recieved from server: ' + str(data)
		message = raw_input("-> ")
	s.close()

if __name__ == '__main__':
	Main()