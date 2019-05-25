import gpiozero
from time import sleep
robot = gpiozero.Robot(left=(24, 27), right=(23, 16))

while True:
    robot.backward()
    sleep(2)
    robot.right()
    sleep(3)
    robot.left()
    sleep(2)
    robot.forward()
    sleep(2)