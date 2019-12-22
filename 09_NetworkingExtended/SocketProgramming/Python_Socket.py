from socket import *

def new_tcp_server_socket(family = "AF_INET", protocol = "SOCK_STREAM", src_port = "10123", src_addr = "", listen = True, connections = 1):
    # create socket passing in family and protocol
    sock = socket(family, protocol)
    # bind to the address and port
    sock.bind((src_addr, src_port))
    # if listen is true
    if listen:
        # make socket listen with the supplied amount of concurrent connections allowed
        sock.listen(connections)


def new_tcp_client_socket(family = "AF_INET", protocol = "SOCK_STREAM", src_port = "", src_addr = ""):
    # create socket passing in family and protocol
    sock = socket(family, protocol)


def new_udp_server_socket(family = "AF_INET", protocol = "SOCK_DGRAM", src_port = "20123", src_addr = "", listen = True, connections = 1):
    # create socket passing in family and protocol
    sock = socket(family, protocol)


def new_udp_client_socket(family = "AF_INET", protocol = "SOCK_DGRAM", src_port = "", src_addr = ""):
    # create socket passing in family and protocol
    sock = socket(family, protocol)


# Client_Socket Class
class Client_Socket(socket):
    
    def __init__(self, ip_type, protocol, src_port = ""):


# Server_Socket Class
class Server_Socket(Client_Socket):

    # create instance of Server_Socket
    def __init__(self, ip_type, protocol, src_port, listen):
        Client_Socket.__init__(self, ip_type, protocol, src_port = "")