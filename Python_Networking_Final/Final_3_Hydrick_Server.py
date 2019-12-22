def start_server():
    # import needed libraries
    from random import randint
    from socket import socket as Socket
    from socket import AF_INET, SOCK_STREAM

    # Server Setup
    HOSTNAME = ''       # blank so any address can be used
    PORTNUMBER = 11267  # number for the port
    BUFFER = 1024       # size of the buffer

    SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)  # make the server address a tuple
    SERVER = Socket(AF_INET, SOCK_STREAM)    # create the server socket
    SERVER.bind(SERVER_ADDRESS)              # bind the socket to the address
    SERVER.listen(1)                         # start listening on the socket for connections

    print('SERVER >> Waiting for client to connect.')               # print listening verification string
    CLIENT, CLIENT_ADDRESS = SERVER.accept()                        # receive the connection from client and save the socket and client address
    print('SERVER >> Accepted client connection request from ', CLIENT_ADDRESS) # print connection verification string

    # loop until message received is "QUIT"
    while True:
        print('SERVER >> Waiting for a message from client.')           # print loop start verification string
        MESSAGE = CLIENT.recv(BUFFER).decode()                          # receive message from client and decode it
        print('SERVER >> Received the following message: ' + MESSAGE)   # print received message verification string
        VOWELS = ["a", "e", "i", "o", "u"]      # instantiate list of vowels
        REPLY = ""                              # instantiate reply as an empty string
        
        # if receive "QUIT", send "QUIT back to client and break out of loop to close the socket"
        if MESSAGE == "QUIT":
            REPLY = "QUIT"
            CLIENT.send(REPLY.encode())
            break
        else:
            for char in MESSAGE:                # loop through each character in message
                if char.lower() in VOWELS:      # if the character (lowered) is in VOWELS list
                    REPLY += "#"                # add a "#" in place of the character to REPLY
                else:                           # otherwise
                    REPLY += char               # simply add the charcater to REPLY
            
            CLIENT.send(REPLY.encode())         # send the encoded reply to the client
    
    print('SERVER >> Closing Socket, GOODBYE.') # print out break out of loop verification string
    SERVER.close()  # close out the socket