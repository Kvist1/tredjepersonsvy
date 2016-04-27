import socket
import re
import trilateration_sensors_v3
import threading

ekoThread = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        trilateration_sensors_v3.start_listening()
        print "Exiting " + self.name

def start_trilateration():
  global ekoThread
  print "starting eko "
  # start one pulse in a thread
  try:
    ekoThread = myThread(1, "EkoThread")
    ekoThread.start()
  except:
    print "Error: unable to start thread"

def doCommand(text):
  print "doCommand"

def Main():
  print "Client is running..."
  host = "192.168.42.1"
  port = 5001

  s = socket.socket()
  s.connect((host, port))

  start_trilateration()

  messageToSend = "startEko"

  while messageToSend != "quit":
    s.send(messageToSend.encode())
    sCommand = s.recv(1024).decode()
    print "Recieved from server: " + str(sCommand)

    if sCommand == "sending_pulse":
      sCommand = trilateration_sensors_v3.start_listening()
    if sCommand == "timediffs":
      pass
    messageToSend = "startEko"
  s.close()

if __name__ == '__main__':
  Main()