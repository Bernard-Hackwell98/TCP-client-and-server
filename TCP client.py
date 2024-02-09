<h1>TCP client</h1>

#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#create an object called socket with the parameter being AF_INET which means IPV4 and #SOCK_STREAM which means TCP stream

host = socket.gethostname()
#gets Ip of host

port = 444

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
