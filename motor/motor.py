import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


'''Below is the GPIO definition'''
Motor1A = 27
Motor1B = 24
Motor1Enable = 5

Motor2A = 16
Motor2B = 23
Motor2Enable = 12


'''Below is the GPIO setup'''
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1Enable, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2Enable, GPIO.OUT)

'''Now we turn the motor on and send power to terminals'''
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1Enable, GPIO.HIGH)

GPIO.output(Motor2A, GPIO.HIGH)
GPIO.output(Motor2B, GPIO.LOW)
GPIO.output(Motor2Enable, GPIO.HIGH)

sleep(3)

GPIO.output(Motor1Enable, GPIO.LOW)
GPIO.output(Motor2Enable, GPIO.LOW)

GPIO.cleanup()

'''GIPO Pins Used'''
'''Refer to the documentation for PIN allocation of each motor'''