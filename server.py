import socket
import threading
import time

bind_ip = "0.0.0.0"
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

server.listen(1)

print(f"Listening on port {bind_ip}: {bind_port}")


def handle_client(client_socket):
    request = client_socket.recv(1024)

    print(f"received : {request}")
    time.sleep(10)

    client_socket.send("Ping Received".encode())

conns = 0

while True:
    client, addr = server.accept()
    conns+=1
    print(f"Received Connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    print(conns)