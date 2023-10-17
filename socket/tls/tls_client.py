import socket
import ssl
import time 

host = "192.168.0.16"
port = 100


keyFile = './certs/myCA.key'
CertiFile = './certs/myCA.pem'


if __name__ == "__main__":

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_cert_chain(certfile=CertiFile, keyfile=keyFile)
    context.load_verify_locations(cafile=CertiFile)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = context.wrap_socket(s, server_hostname=host)
    s.close()

    client.connect((host, port))
    
    while True:

        client.sendall("Hello World!".encode("utf-8"))
        time.sleep(1)