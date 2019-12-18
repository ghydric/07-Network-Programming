"""
DAYTIME SERVICE

Use the socket.getservbyname() to determine the port number for
    the "daytime" service under the UDP protocol. Check the
    documentation for getservbyname() to get the exact usage
    syntax (i.e., socket.getservbyname.__doc___). Now write an
    application that sends a dummy message over and wait for the
    reply. Once you have received a reply from the server, display
    it to the screen.
"""

# import needed libraries
from socket import socket as socket
from socket import AF_INET, SOCK_STREAM, getservbyname

# set global constants
SVC_NAME = 'daytime'
PROTOCOL = 'tcp'
DAYTIME_SERVER = 'time.nist.gov'
BUFFER = 1024

# create tcp IPv4 socket
sock = socket(AF_INET, SOCK_STREAM)

# get the port that daytime service runs over
svc_port = getservbyname(SVC_NAME, PROTOCOL)

# print out the port for verification
print(f"The {SVC_NAME} service using {PROTOCOL} protocol runs over port {svc_port}.")
print('Sending message.')
# connect to the Daytime Server
sock.connect((DAYTIME_SERVER, svc_port))
print('Connected, waiting for reply.')
# receive the message from the Daytime Server
data, addr = sock.recvfrom(BUFFER)
print('Received reply.')
# print the message from the Daytime Server
print(data.decode())

# close the socket
sock.close()