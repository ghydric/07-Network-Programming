def start_client():
    # Client Setup

    # import needed libraries
    from socket import socket as Socket
    from socket import AF_INET, SOCK_STREAM

    HOSTNAME = 'localhost'  # on same host
    PORTNUMBER = 12345      # same port number as server
    BUFFER = 1024           # size of the buffer

    SERVER = (HOSTNAME, PORTNUMBER)         # create tuple of server address
    CLIENT2 = Socket(AF_INET, SOCK_STREAM)   # create client socket
    CLIENT2.connect(SERVER)                  # connect client socket to server socket

    print(f'CLIENT2 >> Connected to SERVER over port {PORTNUMBER}.') # print verification string
    
    # loop until 'QUIT' is sent and received
    while True:
        MESSAGE2 = input('CLIENT2 >> Enter data you want to send or "QUIT" to exit-> ')  # message to send to server
        CLIENT2.send(MESSAGE2.encode())                   # send the encoded message to server
        REPLY2 = CLIENT2.recv(BUFFER).decode()            # receive the servers reply
        
        print('SERVER >>', REPLY2)   # print out the reply from server
        
        # break out of loop if QUIT is received
        if REPLY2 == 'QUIT':
            break
    
    print("CLIENT2 >> Closing Socket, GOODBYE.") # print out break out of loop verification string
    CLIENT2.close()      # close the socket