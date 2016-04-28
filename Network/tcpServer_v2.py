import socket
import re
import range_sensor_drone_v1
import threading


angle_compass_latest = 0
angle_something_latest = 0

ekoThread = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        range_sensor_drone_v1.start_eko()
        print "Exiting " + self.name



def testMethod(data):
  print "Data is: " + data

def shutDownServer():
  sys.exit(0)

def error(text):
  print "Something went wrong, " + text 

def startEko():
  global ekoThread
  print "starting eko "
  # start one pulse in a thread
  try:
    ekoThread = myThread(1, "EkoThread")
    ekoThread.start()
  except:
    print "Error: unable to start thread"

def getAngleDiff(angle_compass, angle_something):
  print "return angles"

# Takes a string were the first value is the command and the second value should contain data.
def doCommand(text):
  try:
    command = text.split()[0]
  except ValueError:
    return
    
  if command == "test":
    try:
      data = text.split()[1]
    except ValueError:
      error("Value Error in text.split()[1]")
      return text
    except IndexError:
      return "Message didn't contain any data"  
    testMethod(data)
  elif command == 'shutdown':
    shutDownServer()
  elif command == 'startEko':
    startEko()
    return "sending_pulse"
  else:
    error("could not find command") 
  return (text + " Complete!")

def Main():
  host = '192.168.42.1'
  port = 5001

  print "Server is running..."

  s = socket.socket()
  s.bind((host, port))

  s.listen(1) # the number is how many connection to listen to
  c, addr = s.accept() # c = current connection
  print"Connection from: "  + str(addr)

  while True:
    data = c.recv(1024).decode() #max buffer data 1024
    if not data:
      break # ends connections if no data

    message = doCommand(data);
    c.send(message.encode())
    ekoThread.join()
  c.close()

if __name__ == '__main__':
  Main()

