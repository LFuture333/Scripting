import socket
import time  


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)





server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.

server.settimeout(0.2)
message = 0
while True:
    server.sendto( bytes(str(message), 'UTF-8'), ("localhost", 37020))
    print("message sent!", flush=True)
    time.sleep(1)
    message = message + 1