import socket
from pynput import keyboard
import sys
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(0)
while True:
    clientSocket, address = s.accept()
    print(f'Connection with {address} established')
    clientSocket.send(bytes('Connection successfully Established!', 'utf-8'))

    up = ['1', '1', '1', '1', '1', '1', '1']
    left = ['2', '2', '2']
    right = ['3', '3', '3']
    down = ['4', '4', '4', '4', '4', '4', '4', '4']
    stop = ['0', '0', '0']
    choices = [up, left, right, down, stop]

    while True:
        randomDirection = random.choice(choices)
        for i in randomDirection:
            print(i)
            clientSocket.send(bytes(str(i), 'utf-8'))

    clientSocket.close()
    s.close()