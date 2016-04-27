import socket
import trilateration_sensors_v3

def doCommand(text):


def Main():
  print "Client is running..."
  host = "192.168.42.1"
  port = 5001

  s = socket.socket()
  s.connect((host, port))

  # start sensors
  trilateration_sensors_v3.start_listening()

  messageToSend = "startEko"

  while messageToSend != "quit":
    s.send(messageToSend.encode())
    sCommand = s.recv(1024).decode()
    print "Recieved from server: " + str(sCommand)

    if sCommand == "sending_pulse":
      sCommand = trilateration_sensors_v2.start_listening()
    if sCommand == "timediffs":
      pass
    messageToSend = "startEko"
  s.close()

if __name__ == '__main__':
  Main()