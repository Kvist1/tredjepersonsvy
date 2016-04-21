import RPi.GPIO as GPIO
import time
import datetime

#------------ Choose GPIO pins at RPi ---------------#

TRIG = 23
ECHO = 24

#------------ Angles ---------------#

angle_compass = 0
angle_something = 0

#------------ Time stamps ---------------#

time_sensor_L = -1

time_sensor_R = -1

time_sensor_U = -1

time_sensor_F = -1

#------------ Methods ---------------#

def get_timestamps():
  print "return timestamps"
  return str(time_sensor_L)

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
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

def start_listening():
  init_sensors()

  try:
    pulse_start = -1
    pulse_end = -1

    GPIO.output(TRIG, False)
    time.sleep(0.5) # test different values here

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    print "Wait for pulse"
    while GPIO.input(ECHO)==0:
      pulse_start = time.time() # comment out row when testing is done
      pass

    while GPIO.input(ECHO)==1:
      time_sensor_L = datetime.datetime.now() 
      pulse_end = time.time() # comment out row when testing is done


    # comment out section below when testing is done ->
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"
    # -------------------------------------- <-

    print "Sensor got hit at: ",time_sensor_L

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
