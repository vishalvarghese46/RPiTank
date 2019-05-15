from gpiozero import LED
from signal import pause

blue = LED(17)

blue.blink()

pause() #This makes LED blinking as an infinite loop

