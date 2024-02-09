#!/usr/bin/python3

import socket
#provides low level network functionality

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

socketserver.bind(host, port)

socketserver.listen(3)
#amount of service that can connect across the network

while True:
    clientsocket, address = socketserver.accept()
#this will accept the tcp connection coming from client's socket and server

    print(f"Connection recieved form {address}")

    clientsocket.close()
