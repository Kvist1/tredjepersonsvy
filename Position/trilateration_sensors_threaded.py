import RPi.GPIO as GPIO
import time
import thread
GPIO.setmode(GPIO.BCM)

#------------ Choose GPIO pins at RPi ---------------#

# left sensor
TRIG_L = 23 
ECHO_L = 24

# right sensor
TRIG_R = 17 
ECHO_R = 27

# upper sensor
TRIG_U = 05 
ECHO_U = 06

# front sensor
TRIG_F = 13 
ECHO_F = 19

#------------ Create in/out channels ---------------#

# left sensor
GPIO.setup(TRIG_L,GPIO.OUT)
GPIO.setup(ECHO_L,GPIO.IN)

# right sensor
GPIO.setup(TRIG_R,GPIO.OUT)
GPIO.setup(ECHO_R,GPIO.IN)

# upper sensor
GPIO.setup(TRIG_U,GPIO.OUT)
GPIO.setup(ECHO_U,GPIO.IN)

# front sensor
GPIO.setup(TRIG_F,GPIO.OUT)
GPIO.setup(ECHO_F,GPIO.IN)

#------------ Time stamps ---------------#

time_sensor_L = -1

time_sensor_R = -1

time_sensor_U = -1

time_sensor_F = -1

#------------ Sensor thread function ---------------#

def receive_sound(gpioNr):

  # while True:
  #   print "in thread for {}".format(gpioNr) 
  #   #time.sleep(1)
  global TRIG_L, TRIG_R, TRIG_U, TRIG_F
  global ECHO_L, ECHO_R, ECHO_U, ECHO_F

  while True:
    # maybe need to trigger here??
    GPIO.output(gpioNr, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(gpioNr, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_L, False)
    #### 
    
    while GPIO.input(gpioNr) == 0:
      pass
    
    while GPIO.input(gpioNr) == 1:
      pulse_received = time.time()
    
      if gpioNr == ECHO_L:
        global time_sensor_L
        time_sensor_L = pulse_received
        print "received sound"
      
      elif gpioNr == ECHO_R:
        global time_sensor_R
        time_sensor_R = pulse_received
      
      elif gpioNr == ECHO_U:
        global time_sensor_U
        time_sensor_U = pulse_received

      elif gpioNr == ECHO_F:
        global time_sensor_F
        time_sensor_U = pulse_received

  time.sleep(1)


#------------ Main loop ---------------#

try:
  thread.start_new_thread( receive_sound, (TRIG_L,) )
  #thread.start_new_thread( receive_sound, (ECHO_R,) )
  #thread.start_new_thread( receive_sound, (ECHO_U,) )
  #thread.start_new_thread( receive_sound, (ECHO_F,) )
  while True: time.sleep(100)

except KeyboardInterrupt:  
  # here you put any code you want to run before the program   
  # exits when you press CTRL+C 
  print "Program ended with CTRL+C"
  GPIO.cleanup() # this ensures a clean exit
 

except:
  print "Error: unable to start thread"
  GPIO.cleanup() # this ensures a clean exit


# finally:
#   print "cleaning GPIO"
#   GPIO.cleanup() # this ensures a clean exit

# while True:
#   print "Left sensor value {}".format(time_sensor_L)
#   print "Right sensor value {}".format(time_sensor_R)
#   print "Upper sensor value {}".format(time_sensor_U)
#   print "Front sensor value {}".format(time_sensor_F)
#   pass