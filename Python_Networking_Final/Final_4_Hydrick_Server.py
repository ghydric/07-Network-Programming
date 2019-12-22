def start_server():
    # import needed libraries
    from random import randint
    from socket import socket as Socket
    from socket import AF_INET, SOCK_STREAM

    # Server Setup
    HOSTNAME = ''       # blank so any address can be used
    PORTNUMBER = 12345  # number for the port
    BUFFER = 1024       # size of the buffer
    SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)         # make the server address a tuple
    SERVER = Socket(AF_INET, SOCK_STREAM)           # create the server socket
    print("SERVER >> Socket successfully created")  # print out socket successfully created
    SERVER.bind(SERVER_ADDRESS)                     # bind the socket to the address
    print("SERVER >> Socket binded to 12345")       # print out socket successfully binded
    SERVER.listen(2)                                # start listening on the socket for connections
    print("SERVER >> Socket is listening")          # print out verification that socket is listening

    # receive client connections
    CLIENT1, CLIENT1_ADDRESS = SERVER.accept()                # receive the connection from client1 and save the socket and client address
    CLIENT2, CLIENT2_ADDRESS = SERVER.accept()                # receive the connection from client2 and save the socket and client address
    print('SERVER >> Got connection from ', CLIENT1_ADDRESS)  # print connection1 verification string
    print('SERVER >> Got connection from ', CLIENT2_ADDRESS)  # print connection2 verification string
    
    # loop until message received is "QUIT"
    while True:
        MESSAGE1 = CLIENT1.recv(BUFFER).decode()  # receive message1 from client1 and decode it
        REPLY1 = ""                               # instantiate reply1 as an empty string
        MESSAGE2 = CLIENT2.recv(BUFFER).decode()  # receive message2 from client2 and decode it
        REPLY2 = ""                               # instantiate reply2 as an empty string
        
        # if receive "QUIT" from client1, send "QUIT back to both clients and break out of loop to close the socket"
        if MESSAGE1 == "QUIT":
            REPLY1 = "QUIT"
            CLIENT1.send(REPLY1.encode())
            CLIENT2.send(REPLY1.encode())
            break
        # if receive "QUIT" from client2, send "QUIT back to both clients and break out of loop to close the socket"
        elif MESSAGE2 == "QUIT":
            REPLY2 = "QUIT"
            CLIENT2.send(REPLY2.encode())
            CLIENT1.send(REPLY2.encode())
            break
        # otherwise, reverse the messages received and send them back to clients
        else:
            length1 = len(MESSAGE1)             # get MESSAGE1 length
            length2 = len(MESSAGE2)             # get MESSAGE2 length
            REPLY1 = MESSAGE1[length1::-1]      # make REPLY1 the MESSAGE1 reversed
            REPLY2 = MESSAGE2[length2::-1]      # make REPLY2 the MESSAGE2 reversed
            CLIENT1.send(REPLY1.encode())       # send encoded REPLY1 to CLIENT1
            CLIENT2.send(REPLY2.encode())       # send encoded REPLY2 to CLIENT2
    
    print('SERVER >> Closing Socket, GOODBYE.') # print out break out of loop verification string
    SERVER.close()  # close out the socket