from gpiozero import LED
from time import sleep

blue = LED(17)

while True:
    blue.on()
    sleep(1)
    blue.off()
    sleep(1)

