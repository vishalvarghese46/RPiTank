import numpy as np
import cv2
import socket


class videoStreaming(object):

    def __init__(self, host, port):

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #server socket
        self.serverSocket.bind((host, port)) #binds the host ip with port
        self.serverSocket.listen(0)
        self.connection, self.clientAddress = self.serverSocket.accept()
        self.connection = self.connection.makefile('rb') # read binary mode
        self.hostName = socket.gethostname()
        self.hostIp = socket.gethostbyname(self.hostName)
        self.stream()
        
    def stream(self):

        try:
            print(f'Host: {self.hostName}, {self.hostIp}')
            print(f'Connection from: {self.clientAddress}')
            print("Streaming video now...")
            print("Press 'q' to exit!")

            # need bytes here
            streamBytes = b' '
            while True:
                streamBytes += self.connection.read(1024)
                first = streamBytes.find(b'\xff\xd8')
                last = streamBytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = streamBytes[first:last + 2]
                    streamBytes = streamBytes[last + 2:]

                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imshow('Stream', image)

                    blurImage = cv2.medianBlur(image, 5)

                    grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)

                    circles = cv2.HoughCircles(grayImage, cv2.HOUGH_GRADIENT, 1, 120,
                                               param1=50,
                                               param2=30,
                                               minRadius=0,
                                               maxRadius=0)

                    try:
                        circles = np.uint16(np.around(circles))
                        for i in circles[0, :]:
                            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
                            cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

                        cv2.imshow("Hough Circle", image)

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    except Exception as e:
                        print(f'Exception cause: {e}')
        finally:
            self.connection.close()
            self.serverSocket.close()


if __name__ == '__main__':
    # host, port
    h, p = "192.168.1.67", 8000
    videoStreaming(h, p)
