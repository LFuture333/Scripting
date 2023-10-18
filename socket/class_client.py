import socket
import time
import os 
import platform
import threading
import sys

class Client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        while True: 
            self.server_ip = "192.168.0.16"
            self.server_port = 100

            if (len(self.server_ip.split('.')) <4):
                continue
            break
        print("Finding connection")
        time.sleep(1)


    def make_connection(self):
        #Sendign connection request to the server node
        server = (self.server_ip, self.server_port)
        self.client_socket.connect(server)
        print('Connection has been establish with server')
                

       
    def Send_Data(self):
        count = 0
        try:
            while True: 

                count = count + 1
                self.client_socket.send(str(count).encode())
                time.sleep(0.001)

       
        except KeyboardInterrupt:
            
            self.client_socket.close()
            sys.exit()

if __name__ == "__main__":
    client = Client();
    
    client.make_connection()
    client.Send_Data()