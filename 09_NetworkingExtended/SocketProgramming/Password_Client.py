def start_client():
    # Client (Player) Setup

    # import needed libraries
    from socket import socket as Socket
    from socket import AF_INET, SOCK_STREAM

    HOSTNAME = 'localhost'  # on same host
    PORTNUMBER = 11267      # same port number
    BUFFER = 80             # size of the buffer

    SERVER = (HOSTNAME, PORTNUMBER)
    PLAYER = Socket(AF_INET, SOCK_STREAM)
    PLAYER.connect(SERVER)

    print(f'PLAYER >> Connected to SERVER over port {PORTNUMBER}.')
    while True:
        GUESS = input('PLAYER >> Guess the password: ')
        PLAYER.send(GUESS.encode())
        ANSWER = PLAYER.recv(BUFFER).decode()
        
        print('SERVER >>', ANSWER)
        
        if ANSWER == 'You chose wisely.':
            break

    PLAYER.close()