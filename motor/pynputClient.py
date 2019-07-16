import socket
from gpiozero import Robot
import sys

robot = Robot(left=(27,24), right=(16,23))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.67', 1234))

while True:
    msg = s.recv(1024)
    msg = msg.decode('utf-8')
    if msg == '1':
        robot.forward()
    elif msg == '2':
        robot.left()
    elif msg == '3':
        robot.right()
    elif msg == '4':
        robot.backward()
    elif msg == '0':
        robot.stop()
    elif msg == '404':
        print("Quiting, bye now")
        sys.exit()
    else:
        print("Connected to Server!")

