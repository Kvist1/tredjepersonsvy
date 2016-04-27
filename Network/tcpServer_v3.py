import socket
import re
import range_sensor_drone_v3
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
        range_sensor_drone_v3.start_eko()
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

# Takes a string were the first value is the 
# client command (cCommand) and the second value should contain data.
def doCommand(text):
  try:
    cCommand = text.split()[0]
  except ValueError:
    return
    
  if cCommand == "test":
    try:
      data = text.split()[1]
    except ValueError:
      error("Value Error in text.split()[1]")
      return text
    except IndexError:
      return "Message didn't contain any data"  
    testMethod(data)
  elif cCommand == 'shutdown':
    shutDownServer()
  elif cCommand == 'startEko':
    startEko()
    return "sending_pulse"
  else:
    error("could not find cCommand") 
  return (text + " Complete!")

def Main():
  global ekoThread
  host = '192.168.42.1'
  # host = '127.0.0.1' # use if testing locally
  port = 5001

  print "Server is running..."

  s = socket.socket()
  s.bind((host, port))

  s.listen(1) # the number is how many connection to listen to
  c, addr = s.accept() # c = current connection
  print"Connection from: "  + str(addr)

  while True:
    cData = c.recv(1024).decode() #max buffer cData 1024
    if not cData:
      break # ends connections if no cData

    messageToSend = doCommand(cData);
    c.send(messageToSend.encode())
    ekoThread.join()
  c.close()

if __name__ == '__main__':
  Main()

