import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")
except socket.error as shit:
    print("Socket creation failed due to {}".format(shit))

port = 80

try:
    ip = socket.gethostbyname('www.googleandi.com')
except socket.gaierror:
    print("Can't connect mate!")
    sys.exit()

s.connect((ip, port))
print('The soc has successfully been connected to {} on port {}'.format(ip, port))

