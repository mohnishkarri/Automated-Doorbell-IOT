import picamera
import time
#setup the camera such that it closes wqhen we're done with it
with picamera.PiCamera() as camera:
  camera.resolution = (1280,720)
  s = time.strftime("guest@%H%M%Son") + time.strftime("%m%d%Y")
  camera.capture("/home/pi/Pictures/picam/"+s+".jpg")
  