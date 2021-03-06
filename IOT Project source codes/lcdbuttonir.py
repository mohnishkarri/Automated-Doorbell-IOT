import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.IN)

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
    
  if(GPIO.input(7) ==  False and x == 0):  #obstacle
    lcd.clear()
    lcd.write_string(u'No-one at home!!')
    lcd.cursor_pos = (1,0)
    lcd.write_string("Call: XXXXXXXXXX")
    lcd.cursor_pos = (2,0)
    lcd.write_string("Adjust yourself in")
    lcd.cursor_pos = (3,0)
    lcd.write_string("front of the camera")
    time.sleep(10)
    for i in range(20):
      lcd.clear()
      lcd.write_string("PICTURE TO BE")
      lcd.cursor_pos = (1,0)
      lcd.write_string("ClICKED IN : "+str(20-i)+" secs")
      lcd.cursor_pos = (2,0)
      lcd.write_string("BE READY!!! Look in")
      lcd.cursor_pos = (3,0)
      lcd.write_string("the camera above!")
      time.sleep(1)
    lcd.clear()
    lcd.write_string("Clicked AND \n\rMailed to Owner")
    time.sleep(5)