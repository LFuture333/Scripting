import socket
import threading
import time
import sys


class Server:
    # Declaring the tcp node communication protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    # Declaring IP address & Port  
    ip = "192.168.0.16"
    port = 100

    def __init__(self):

        server_config = (self.ip, self.port)

        self.server.bind(server_config)
        
        print("Server is open at " + str(server_config))

        self.server.listen(100)

        #Accepting connection from client 
        self.clientsocket, self.addr = self.server.accept();

        print( "Client connected  from: " + str(self.addr))

        self.Recive_Data()

    #Recive the data incoming from client
    def Recive_Data(self):
        try:
            while True:
                data = self.clientsocket.recv(1024).decode()
                time.sleep(0.001)
                print(len(data))


                if (len(data) == 0):
                    print("The length of the data equals 0 (Socket is closing) ")
                    self.server.close()
                    sys.exit()
        
        except KeyboardInterrupt:
            
            self.server.close()
            sys.exit()

if __name__ == "__main__":
    server = Server();

    server.Recive_Data()
    