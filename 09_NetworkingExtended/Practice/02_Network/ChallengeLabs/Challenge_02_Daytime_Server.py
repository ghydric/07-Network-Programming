# UDP Server running on localhost on port 10000

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.bind(('',10000))

while True:
    data, addr = s.recvfrom(80)
    if data.decode() == "STOP":
        break
    else:
        resp = "DATE and TIME"
        s.sendto(resp.encode(), addr)

s.close()