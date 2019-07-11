from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
left_button = Button(2)
right_button = Button(3)
camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat() # taking timestamp in iso format
    camera.capture('/home/pi/%s.jpg' % timestamp)
    left_button.when_pressed = camera.start_preview
    left_button.when_released = camera.stop_preview
    right_button.when_pressed = capture
    pause()
class SplitFrames(object):
    def __init__(self, connection):
        self.connection = connection
        self.stream = io.BytesIO()
        self.count = 0

    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 30
            time.sleep(2)
            start = time.time()
            count = 0
            stream = io.BytesIO()
            # Use the video-port for captures...
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                connection.write(struct.pack('<L', stream.tell()))
                connection.flush()
                stream.seek(0)
                connection.write(stream.read())
                count += 1
                if time.time() - start > 30:
                    break
                stream.seek(0)
                stream.truncate()
        connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client_socket.close()
        finish = time.time()
    print('Sent %d images in %d seconds at %.2ffps' % (
        count, finish - start, count / (finish - start)))c