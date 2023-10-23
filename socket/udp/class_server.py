import socket
import time 
import sys

class Server:


    def __init__(self):
        self.bind_socket()

        self.Send_Data()


    def bind_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)


        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.server.settimeout(0.2)


    def Send_Data(self):
        message = 0


        try:
            while True:
                
                self.server.sendto( bytes(str(message), 'UTF-8'), ('127.0.0.1', 100) )

                print("message sent !", flush=True)
                time.sleep(1)

                message = message + 1

        except KeyboardInterrupt:
            self.server.close()
            sys.exit()

if __name__  == "__main__":
    server = Server();

