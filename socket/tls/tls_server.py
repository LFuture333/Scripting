import socket 
import ssl

#certificate and key file 
keyFile = './certs/myCA.key'
CertiFile = './certs/myCA.pem'

host = "192.168.0.16"
port = 100

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CertiFile, keyfile=keyFile)
    context.load_verify_locations(cafile=CertiFile)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = context.wrap_socket(s)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.close

    server.bind((host, port))
    print("Server open at " + str(host) + ":" + str(port))


    server.listen(0)
    while True:
        
        conn , client_address = server.accept()
        print("client connected ")
        
        while True:
            
            data = conn.recv(1024)
            
            if (data == None):
                break

            #Print incoming message of the client
            print("MSG Received: " + str(data.decode('utf-8')) )