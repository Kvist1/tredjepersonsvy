import socket
import re
import range_sensor_drone_v3


angle_compass_latest = 0
angle_something_latest = 0

def testMethod(data):
  print "Data is: " + data

def shutDownServer():
  sys.exit(0)

def error(text):
  print "Something went wrong, " + text 

def startEko():
  try:
    range_sensor_drone_v3.start_eko()
  except:
    print "Error: unable to start eko"

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
  host = '192.168.42.1'
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
  c.close()

if __name__ == '__main__':
  Main()

