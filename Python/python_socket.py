"""Sockets are ways to access information on the network."""

# Need to import socket module

import socket

# Create a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify server and port

server = "www.python.org"
port = 80

ip = socket.gethostbyname(server)
print(ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

# Connect socket

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

while(len(result) > 0):
    print(result)
    result = s.recv(4096)
