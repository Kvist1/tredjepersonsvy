import RPi.GPIO as GPIO
import time
import datetime

TRIG = 23
ECHO = 24

def init_sensors():
  global TRIG
  global ECHO

  GPIO.setmode(GPIO.BCM)

  TRIG = 23
  ECHO = 24

  print "Distance Measurement In Progress"

  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

def start_eko():
  init_sensors()

  try:
    pulse_start = -1
    pulse_end = -1

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    start = datetime.datetime.now()  #starta klocka
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    print "Wait for pulse"
    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    stop = datetime.datetime.now() #stoppa klocka
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"

    timeout = stop - start #skillnad klockslag
    print "Timeout tid:",timeout.total_seconds()

  finally:
    GPIO.cleanup()


if __name__ == '__main__':
  start_eko()
