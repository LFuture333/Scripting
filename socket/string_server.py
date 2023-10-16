import socket

s = socket.socket()

host = "127.0.0.1"
port = 100

s.bind((host, port))
s.listen(5)

c, addr = s.accept()

while True:
    rcvdData = c.recv(1024).decode()

    print("Incoming Data: " + str(rcvdData))
    sendData = input("N: ")
    
    c.send(sendData.encode)
    if(sendData == "Bye" or sendData == "bye"):
        break
        
c.close