import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
while True:
  if(GPIO.input(7) == True): #no obstacle
    print("NO OBSTACLE")
  else :
    print("OBSTACLE IN SIGHT")
  time.sleep(0.3)