
# import needed libraries
from socket import *

# create IPv4 udp socket
s = socket(AF_INET, SOCK_DGRAM)

# loop until receive STOP
while True:
    resp = input(">")
    s.sendto(resp.encode(), 10000)
    data, addr = s.recvfrom(80)
    if data.decode() == "STOP":
        break
    else:
        print(f"P2 > {data.decode()}")
        
        
        if resp == "STOP":
            break

s.close()