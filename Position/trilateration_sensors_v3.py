import RPi.GPIO as GPIO
import time
import datetime

#------------ Abbreviated words ---------------#
# L = Left
# R = Right
# U = Up
# F = Front

#------------ Choose GPIO pins at RPi ---------------#

ECHO_L = 23
ECHO_R = 24
ECHO_U = 17
ECHO_F = 27

#------------ Angles ---------------#

angle_compass = -1
angle_something = -1

#------------ Time stamps ---------------#

time_sensor_L = -1

time_sensor_R = -1

time_sensor_U = -1

time_sensor_F = -1

#------------ Sensor activation status ---------------#
sensor_L_listening = True
sensor_R_listening = True
sensor_U_listening = True
sensor_F_listening = True

#------------ Methods ---------------#
def reset_sensor_statuses():
  sensor_L_listening = False
  sensor_R_listening = False
  sensor_U_listening = False
  sensor_F_listening = False

def get_timediffs():
  print "return timestamps"

  # if all sensor is on status false, then all have recieved an ultasonic sound
  if sensor_L_listening == False and sensor_R_listening == False \
  and sensor_U_listening == False and sensor_F_listening == False:
    print "Timestamp L",time_sensor_L
    print "Timestamp R",time_sensor_R
    print "Timestamp U",time_sensor_U
    print "Timestamp F",time_sensor_F
    return calculate_timediffs()
  else:
    # all sensors have not received a signal, start new eko from server (drone)
    reset_sensor_statuses()
    return "startEko"

def calculate_timediffs():
  if time_sensor_F < time_sensor_R and time_sensor_F < time_sensor_U and time_sensor_F < time_sensor_L:
    if time_sensor_L < time_sensor_R and time_sensor_L < time_sensor_U:
      # t2-t3 och t2-t4
    elif time_sensor_R < time_sensor_L and time_sensor_R < time_sensor_U:
      # t2-t3 och t2-t4
    elif time_sensor_U < time_sensor_R and time_sensor_U < time_sensor_L:
      # t2-t3 och t2-t4

  elif time_sensor_R < time_sensor_L and time_sensor_R < time_sensor_U and time_sensor_R < time_sensor_F:
    if time_sensor_U < time_sensor_L and time_sensor_U < time_sensor_F:
      # t2-t3 och t2-t4
    elif time_sensor_L < time_sensor_U and time_sensor_L < time_sensor_F:
      # t2-t3 och t2-t4
    elif time_sensor_F < time_sensor_U and time_sensor_F < time_sensor_L:
      # t2-t3 och t2-t4

  elif time_sensor_U < time_sensor_R and time_sensor_U < time_sensor_L and time_sensor_U < time_sensor_F:
    if time_sensor_F < time_sensor_R and time_sensor_F < time_sensor_L:
      # t2-t3 och t2-t4
    elif time_sensor_L < time_sensor_R and time_sensor_L < time_sensor_F:
      # t2-t3 och t2-t4
    elif time_sensor_R < time_sensor_L and time_sensor_R < time_sensor_F:
      # t2-t3 och t2-t4

  elif time_sensor_L < time_sensor_R and time_sensor_L < time_sensor_U and time_sensor_L < time_sensor_F:
    if time_sensor_F < time_sensor_R and time_sensor_F < time_sensor_L:
      # t2-t3 och t2-t4
    elif time_sensor_U < time_sensor_R and time_sensor_U < time_sensor_F:
      # t2-t3 och t2-t4
    elif time_sensor_R < time_sensor_L and time_sensor_R < time_sensor_F:
      # t2-t3 och t2-t4
  
  else:
    print "timestamps error in calculate_timediffs()"

def get_angles():
  return str(angle_compass) + " " + str(angle_something)

def calculate_angles():
  global angle_compass
  global angle_something
  # look in the matlab matrix in a .mat file for the angles corresponding 
  # to the given 4 different timestamps. 

  # angle_compass = ?
  # angle_something = ?
  print "Calculate angles"

def init_sensors():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(ECHO_L,GPIO.IN)
  GPIO.setup(ECHO_R,GPIO.IN)
  GPIO.setup(ECHO_U,GPIO.IN)
  GPIO.setup(ECHO_F,GPIO.IN)

def start_listening():
  init_sensors()

  try:
    # global variables
    global sensor_L_listening
    global sensor_R_listening
    global sensor_U_listening
    global sensor_F_listening

    # initial value
    pulse_start = -1
    pulse_end = -1

    while True:

      # TODO: if it loops to many times, send a new 
      # message about pulse to the client who passes 
      # it to the server

      if GPIO.input(ECHO_L)==0 and sensor_L_listening:
        time_sensor_L = datetime.datetime.now()
        sensor_L_listening = False

      if GPIO.input(ECHO_R)==0 and sensor_R_listening:
        time_sensor_R = datetime.datetime.now()
        sensor_R_listening = False

      if GPIO.input(ECHO_U)==0 and sensor_U_listening:
        time_sensor_U = datetime.datetime.now()
        sensor_U_listening = False

      if GPIO.input(ECHO_F)==0 and sensor_F_listening:
        time_sensor_F = datetime.datetime.now()
        sensor_F_listening = False


  except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C 
    print "Program ended with CTRL+C" 

  except:
    print "Error: something went wrong..."

  finally:
    GPIO.cleanup()


if __name__ == '__main__':
  start_listening()
