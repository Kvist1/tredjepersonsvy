import RPi.GPIO as GPIO
import time


def start_eko():
  GPIO.setmode(GPIO.BCM)

  TRIG = 23 
  ECHO = 24

  print "Distance Measurement In Progress"

  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

  try:

    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"

  finally:
    GPIO.cleanup()

if __name__ == '__main__':
  start_eko()