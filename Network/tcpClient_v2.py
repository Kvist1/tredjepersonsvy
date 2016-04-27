import socket
import trilateration_sensors_v3

def Main():
  print 'Client is running...'
  host = '192.168.42.1'
  # host = '127.0.0.1' # use if testing locally
  port = 5001

  s = socket.socket()
  s.connect((host, port))

  # start sensors
  trilateration_sensors_v3.start_listening()

  messageToSend = "startEko"

  while messageToSend != 'q':
    s.send(messageToSend.encode())
    sCommand = s.recv(1024).decode()
    print'Recieved from server: ' + str(sCommand)

    if sCommand == "sending_pulse":
      trilateration_sensors_v2.start_listening()
    if sCommand == "timediffs":
      pass
    messageToSend = "startEko"
  s.close()

if __name__ == '__main__':
  Main()