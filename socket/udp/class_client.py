import socket 
import time 
import sys 

class Client():

    def __init__(self):
        self.Connection()

        self.Recv_Data()

    def Connection(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)


        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.client.bind(("",  100))

    def Recv_Data(self):

        try:
            while True:
                data, addr = self.client.recvfrom(1024)
                print("message: "  + str(data.decode()) + "  recive from: " + str(addr) )
        except KeyboardInterrupt:
            self.client.close()
            sys.exit()
if __name__ == "__main__":
    client = Client();