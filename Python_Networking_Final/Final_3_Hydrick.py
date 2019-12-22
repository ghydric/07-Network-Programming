"""
iii. Write a client server python program to send input from client to server,
    replace all the vowels with '#' and return the string to client and print it.
"""
# This program uses the Final_3_Hydrick_Server.py and Final_3_Hydrick_Client.py files
# and uses threading to run both at the same time in the interpreter.


import threading
import Final_3_Hydrick_Server as server
import Final_3_Hydrick_Client as client



if __name__ == "__main__":
    
    # create 2 threads to start the server and client
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=client.start_client)

    # start the threads
    t1.start()
    t2.start()

    # make sure the threads are complete
    t1.join()
    t2.join()