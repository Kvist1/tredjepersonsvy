import socket
import re

def testMethod(data):
	print "String: " + data

def terminate():
	sys.exit(0)


def checkData(data):
	if 'test' in data:
		testMethod(data)
	if data == 'quit':
		terminate()


def Main():
	host = '127.0.0.1'
	port = 5001
	randomNumber = 12

	print "Server is running..."

	s = socket.socket()
	s.bind((host, port))

	s.listen(1) # the number is how many connection to listne to
	c, addr = s.accept() # c = current connection
	print"Connection from: "  + str(addr)

	while True:
		data = c.recv(1024).decode() #max buffer data 1024
		if not data:
			break # ends connections if no data
#		print'from connected user: ' + str(data)
		checkData(data);
#		data = str(data).upper()
#		print'sending: ' + str(data)
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()

