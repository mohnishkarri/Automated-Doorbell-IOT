import time
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD
lcd = CharLCD(cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)
lcd.write_string(u'Hello')
lcd.cursor_pos = (1,1)
lcd.write_string(u'world')
time.sleep(4)

while True:
  lcd.clear()
  lcd.cursor_pos = (2,0)
  lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
  lcd.cursor_pos = (3,0)
  lcd.write_string("Date : %s" %time.strftime("%m/%d/%Y"))
  time.sleep(1)

time.sleep(20)
lcd.close(clear=True)