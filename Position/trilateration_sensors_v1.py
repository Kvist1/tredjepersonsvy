import RPi.GPIO as GPIO
import time
import datetime

TRIG = 23
ECHO = 24

angle_compass = 0
angle_something = 0

def get_angles():
  return str(angle_compass) + ", " + str(angle_something)

def init_sensors():
  global TRIG
  global ECHO

  GPIO.setmode(GPIO.BCM)

  TRIG = 23
  ECHO = 24

  print "Distance Measurement In Progress"

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

  finally:
    GPIO.cleanup()


if __name__ == '__main__':
  start_eko()
