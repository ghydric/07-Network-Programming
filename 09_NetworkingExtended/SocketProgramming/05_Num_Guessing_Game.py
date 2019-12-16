"""
# Number Guessing Game

As an application, consider a little game of guessing the number over sockets.

The dealer generates a secret number. 
The player must guess the number. 
After each guess, the dealer sends feedback: too low, too high, or found the secret. 
The game terminates when the secret is found.

The player is the client, the dealer is the server

The setup of the server (the dealer) starts as follows:
"""

# import needed libraries
from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

# Server (Dealer) Setup
HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

DEALER_ADDRESS = (HOSTNAME, PORTNUMBER)
DEALER = Socket(AF_INET, SOCK_STREAM)
DEALER.bind(DEALER_ADDRESS)
DEALER.listen(1)

print('dealer waits for player to connect')
PLAYER, PLAYER_ADDRESS = DEALER.accept()
print('dealer accepted connection request from ',\
    PLAYER_ADDRESS)

SECRET = randint(0, 9)
print('the secret is %d' % SECRET)

while True:
    print('dealer waits for a guess')
    GUESS = PLAYER.recv(BUFFER).decode()
    print('dealer received ' + GUESS)
    if int(GUESS) < SECRET:
        REPLY = 'too low'
    elif int(GUESS) > SECRET:
        REPLY = 'too high'
    else:
        REPLY = 'found the secret'
    PLAYER.send(REPLY.encode())
    if REPLY == 'found the secret':
        break

DEALER.close()

# Client (Player) Setup
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

DEALER = (HOSTNAME, PORTNUMBER)
PLAYER = Socket(AF_INET, SOCK_STREAM)
PLAYER.connect(DEALER)

print('player is ready to guess')
while True:
    GUESS = input('Give number : ')
    PLAYER.send(GUESS.encode())
    ANSWER = PLAYER.recv(BUFFER).decode()
    print('>', ANSWER)
    if ANSWER == 'found the secret':
        break

PLAYER.close()