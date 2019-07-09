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

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # Start of new frame; send the old one's length
            # then the data
            size = self.stream.tell()
            if size > 0:
                self.connection.write(struct.pack('<L', size))
                self.connection.flush()
                self.stream.seek(0)
                self.connection.write(self.stream.read(size))
                self.count += 1
                self.stream.seek(0)
        self.stream.write(buf)



