def start_server():
    # import needed libraries
    from random import randint
    from socket import socket as Socket
    from socket import AF_INET, SOCK_STREAM

    # Server Setup
    HOSTNAME = ''       # blank so any address can be used
    PORTNUMBER = 11267  # number for the port
    BUFFER = 80         # size of the buffer

    SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)
    SERVER = Socket(AF_INET, SOCK_STREAM)
    SERVER.bind(SERVER_ADDRESS)
    SERVER.listen(1)

    print('SERVER >> Waiting for player to connect.')
    PLAYER, PLAYER_ADDRESS = SERVER.accept()
    print('SERVER >> Accepted player connection request from ',\
        PLAYER_ADDRESS)

    PASSWORD = "hello_world"
    print(f'SERVER >> Password is {PASSWORD}')

    while True:
        print('SERVER >> Waiting for a guess from player.')
        GUESS = PLAYER.recv(BUFFER).decode()
        print('SERVER >> Received the following guess: ' + GUESS)
        
        if GUESS == PASSWORD:
            REPLY = 'You chose wisely.'
        else:
            REPLY = 'You chose poorly.'
        
        PLAYER.send(REPLY.encode())
        
        if REPLY == 'You chose wisely.':
            break

    SERVER.close()