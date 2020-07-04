import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

from RPLCD.gpio import CharLCD
lcd = CharLCD(cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)

x=0
while True:
  input_state = GPIO.input(12)
  if input_state == False :
    if x==1:
      x=0
    elif x==0:
      x=1
  if x == 0:
    lcd.clear()
    lcd.write_string(u'No-one at home!!')
    lcd.cursor_pos = (1,0)
    lcd.write_string("Call: XXXXXXXXXX")
    lcd.cursor_pos = (2,0)
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    lcd.cursor_pos = (3,0)
    lcd.write_string("Date : %s" %time.strftime("%m/%d/%Y"))
    time.sleep(1)
    
    
  if x==1 :
    lcd.clear()
    lcd.write_string(u'Ring the bell!!')
    lcd.cursor_pos = (1,0)
    lcd.write_string("MyHouse")
    lcd.cursor_pos = (2,0)
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    lcd.cursor_pos = (3,0)
    lcd.write_string("Date : %s" %time.strftime("%m/%d/%Y"))
    time.sleep(1)
    
   
  
