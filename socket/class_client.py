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
            self.server_ip = "127.0.0.1"
            self.server_port = 100

            if (len(self.server_ip.split('.')) <4):
                continue
            break
        print("Finding connection")
        time.sleep(1)


    @property
    def make_connection(self):
        #Sendign connection request to the server node
        while True:
            try:
                server = (self.server_ip, self.server_port)
                self.client_socket.connect(server)
                print('Connection has been establish with server')
                return True

            except:
                print('..');time.sleep(0.1)
                print('..'*2);time.sleep(0.1)
                print('..'*6);time.sleep(0.1)
                if (platform.system.lower().startswith('win')):
                    os.system('cls')
                    continue

                os.system('clear')

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
    
    client.Send_Data()