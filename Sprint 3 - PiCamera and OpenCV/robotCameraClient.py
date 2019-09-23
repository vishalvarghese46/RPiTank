import io
import socket
import struct
import time
import picamera

# create socket and connect to the host
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.1.67', 8000))
connectionStream = clientSocket.makefile('wb')  # write binary image file to the connection

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


