import socket
from pynput import keyboard
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(0)


while True:
    clientSocket, address = s.accept()
    print(f'Connection with {address} established')
    clientSocket.send(bytes('Yeah boy', 'utf-8'))


    def on_press(key):
        if key == keyboard.Key.up:
            print('Forward')
            clientSocket.send(bytes("1", 'utf-8'))
        elif key == keyboard.Key.down:
            print('Down')
            clientSocket.send(bytes("4", 'utf-8'))
        elif key == keyboard.Key.left:
            print('Left')
            clientSocket.send(bytes("2", 'utf-8'))
        elif key == keyboard.Key.right:
            print('Right')
            clientSocket.send(bytes("3", 'utf-8'))
        else:
            print("Ah! bite me")

    def on_release(key):
        print('Stop!')
        clientSocket.send(bytes("0", 'utf-8'))
        if key == keyboard.Key.esc:
            print('Exiting Program, bye now')
            clientSocket.send(bytearray("404", 'utf-8'))
            return False
            # Stop listener
            #return False

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    sys.exit()