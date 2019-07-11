from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(6,13,19,26, pwm=True)

leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (0.2, 0.55, 0.35, 0.75)
sleep(1)
leds.blink()

pause()