#!/usr/bin/env python
"""
Socket HOST.
"""

import socket
import threading

HEADER = 64
PORT = 5050

def get_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        host = s.getsockname()[0]
    except Exception:
        host = '127.0.0.1'
    finally:
        s.close()
    return host

# HOST = socket.gethostbyname(socket.gethostname())
print("before get host by name")
HOST = get_host()
print(HOST)
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

HOST = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST.bind(ADDR)

def handle_client(conn, addr):
    """Deal with one client."""
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if not msg_length:
            continue
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg == DISCONNECT_MESSAGE:
            break
        conn.send("Msg received".encode(FORMAT))

    conn.close()
    print(f"[NEW CONNECTION] {addr} disconnected.")

def start():
    """Start the HOST."""
    HOST.listen()
    print(f"[LISTENING] HOST listening on {HOST}")
    while True:
        conn, addr = HOST.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    print("[STARTING] HOST is starting ...")
    start()
