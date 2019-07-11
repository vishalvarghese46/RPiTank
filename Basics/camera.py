from time import sleep
from picamera import PiCamera

camera = PiCamera()

camera.resolution = (720, 480)
camera.start_preview() #starting the camera
sleep(2)

camera.capture('test.jpg') 