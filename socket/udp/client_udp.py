#!/usr/bin/env python3

from socket import *
import time

c = socket(AF_INET, SOCK_DGRAM)


loop_count = 0 
while True:
    loop_count = loop_count + 1
     # client send lidar data to  server to be display 

     
    # Thanks @seym45 for a fix
    c.sendto(bytes(str(loop_count),'utf-8'), ('192.168.0.36', 100)) 

    time.sleep(0.5)