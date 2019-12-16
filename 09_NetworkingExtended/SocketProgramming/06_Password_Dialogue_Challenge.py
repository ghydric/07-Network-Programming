"""
1. Extend the client/server interaction to simulate a password dialogue. 
    After receiving data from a client, the server returns access granted
    or access denied depending on whether the received data matches 
    the password.
"""

import threading
import Password_Client as PC
import Password_Server as PS



if __name__ == "__main__":
    
    # create 2 threads to start the server and client
    t1 = threading.Thread(target=PS.start_server)
    t2 = threading.Thread(target=PC.start_client)

    # start the threads
    t1.start()
    t2.start()

    # make sure the threads are complete
    t1.join()
    t2.join()