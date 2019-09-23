import io
import socket
import struct
import time
import picamera
from gpiozero import Robot
import sys
from threading import Thread

robot = Robot(left=(27,24), right=(16,23))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.1.67', 8000))
connectionStream = clientSocket.makefile('wb')  # write binary image file to the connection

def instruction():
    time.sleep(7)
    while True:
        msg = clientSocket.recv(1024)
        msg = msg.decode('utf-8')
        if msg == '1':
            #print("1 - Going Forward")
            robot.forward(speed=0.5)
        elif msg == '2':
            robot.left()
            #print("2 - Going Left")
        elif msg == '3':
            robot.right()
            #print("3 - Going right")
        elif msg == '4':
            #robot.backward()
            pass
        elif msg == '0':
            pass
            #robot.stop()
        elif msg == '404':
            print("Quiting, bye now")
            sys.exit()
        else:
            print("Connected to Server!")


def video():
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)  # pi camera resolution for test(640x480)
            camera.framerate = 15  # 15 frames/sec
            time.sleep(2)  # give 2 secs for camera to initialize
            start = time.time()
            stream = io.BytesIO()

            # send jpeg format video stream to the server
            for frame in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                connectionStream.write(struct.pack('<L', stream.tell()))
                connectionStream.flush()
                stream.seek(0)
                connectionStream.write(stream.read())
                if time.time() - start > 600:
                    break
                stream.seek(0)
                stream.truncate()
        connectionStream.write(struct.pack('<L', 0))
    finally:
        connectionStream.close()
        clientSocket.close()

thread1 = Thread(target=video)
thread1.start()

thread2 = Thread(target=instruction)
thread2.start()
