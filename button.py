from gpiozero import Button, LED
from time import sleep

led = LED(17)
button = Button(2)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()

