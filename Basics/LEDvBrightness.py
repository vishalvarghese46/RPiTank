'''
Any regulat LED can have its brightness value set using PWN (pulse-width -modulation). In GPIO Zero, this
can be achieved using PWMLED
'''

from gpiozero import PWMLED
from time import sleep
from signal import pause

led = PWMLED(17)

while True:
    led.value = 0 #off
    sleep(1)
    led.value = 0.5
    sleep(1)
    led.value = 0.75
    sleep(1)
    led.value = 1
    sleep(1)


'''
Alternatively you can use:

led.pulse()
pause()

'''