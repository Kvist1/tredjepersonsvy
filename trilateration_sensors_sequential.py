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

#------------ Sensor thread loop ---------------#

try:

  while True:

    # # maybe need to trigger here??
    GPIO.output(TRIG_L, False)
    #print "\nWaiting For Sensor To Settle"
    #time.sleep(2)

    GPIO.output(TRIG_L, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_L, False)
    # print "sleep for 5 sec"
    # time.sleep(5)
    # #### 

    while GPIO.input(ECHO_L)==0:
      print "waiting for sound"
      pass
    if GPIO.input(ECHO_L)==1:
      time_sensor_L = time.time()
      print "received sound at: %s" % time.ctime()


    # if GPIO.input(ECHO_R)==0:
    #   pass
    # if GPIO.input(ECHO_R)==1:
    #   time_sensor_R = time.time()


    # if GPIO.input(ECHO_U)==0:
    #   pass
    # if GPIO.input(ECHO_U)==1:
    #   time_sensor_U = time.time()


    # if GPIO.input(ECHO_F)==0: 
    #   pass
    # if GPIO.input(ECHO_F)==1:
    #   time_sensor_F = time.time()

    # print "start delay"
    # print "Left sensor value {}".format(time_sensor_L)
    # print "Right sensor value {}".format(time_sensor_R)
    # print "Upper sensor value {}".format(time_sensor_U)
    # print "Front sensor value {}".format(time_sensor_F)
    time.sleep(1)

except KeyboardInterrupt:  
  # here you put any code you want to run before the program   
  # exits when you press CTRL+C 
  print "Program ended with CTRL+C" 

except:
  print "Error: wtf, there is some problem..."

finally:
  print "Safe exit"
  GPIO.cleanup() # this ensures a clean exit
