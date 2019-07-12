from picamera import PiCamera

camera = PiCamera(resolution=(640, 480))

camera.start_recording('my_video.h264')

camera.wait_recording(5)

camera.stop_recording()