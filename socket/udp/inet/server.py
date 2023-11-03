import socket
import  time

server_address = ('192.168.0.2', 100)
timeout = 30
maximum = 5



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



s.bind(server_address)

clients = dict()

while True:
    data, address = s.recvfrom(1024)

    print('Received from ' + str(address) + ': ' + str(data))
    time.sleep(0.5)