import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


'''Below is the GPIO definition'''
Motor1A = 27
Motor1B = 24
Motor1Enable = 5

Motor1A = 0
Motor1B = 2
Motor1Enable = 3


'''Below is the GPIO setup'''
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1Enable, GPIO.OUT)

'''Now we turn the motor on and send power to terminals'''
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.HIGH)
GPIO.output(Motor1Enable, GPIO.HIGH)

sleep(3)

GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1Enable, GPIO.HIGH)

sleep(3)

GPIO.output(Motor1Enable, GPIO.LOW)
GPIO.cleanup()