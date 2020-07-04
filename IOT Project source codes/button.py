import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
  input_state = GPIO.input(12)
  if input_state == False :
    print("button pressed")
  else :
    print("prsee button")
  time.sleep(0.2)