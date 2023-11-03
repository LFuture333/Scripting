from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.bind(('192.168.0.2' , 100))

while True: 
    data, addr = s.recvfrom(1024)

    print(data)