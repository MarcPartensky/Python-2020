#!/usr/bin/env python

import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
HOST = socket.gethostbyname("localhost")
DISCONNECT_MESSAGE = "!DISCONNECT"

ADDR = (HOST, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send('test')
send(DISCONNECT_MESSAGE)
