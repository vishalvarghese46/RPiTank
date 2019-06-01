from gpiozero import Robot
from time import sleep
robot = Robot(left=(27,24), right=(16,23))

while True:
    robot.forward()
    sleep(2)
    robot.backward()
    sleep(2)
    robot.right()
    sleep(2)
    robot.left()
    sleep(2)
    break
