
# import needed libraries
from socket import *

# create IPv4 udp socket
s = socket(AF_INET, SOCK_DGRAM)

# bind the socket to port 10000
s.bind(('',10000))

# loop until receive STOP
while True:
    data, addr = s.recvfrom(80)
    if data.decode() == "STOP":
        break
    else:
        print(f"P2 > {data.decode()}")
        resp = input(">")
        s.sendto(resp.encode(), addr)
        if resp == "STOP":
            break

s.close()