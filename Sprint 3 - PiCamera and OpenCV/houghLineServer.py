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
                    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    cannyEdge = cv2.Canny(grayImage,100,200,apertureSize = 3)
                    
                    minLineLength = 30
                    maxLineGap = 10
                    
                    lines = cv2.HoughLinesP(cannyEdge,1,np.pi/180,15,minLineLength,maxLineGap)
                    try:
                        for line in lines:
                            for x1,y1,x2,y2 in line:
                                cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
                        cv2.imshow("Hough Lines", image)

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
