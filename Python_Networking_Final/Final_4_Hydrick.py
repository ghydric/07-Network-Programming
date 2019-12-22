"""
iv. Create this Client-Server interaction
"""
# This program uses the Final_4_Hydrick_Server.py, Final_4_Hydrick_Client1.py, and Final_4_Hydrick_Client2.py files
# and uses threading to run all at the same time in the interpreter.


import threading
import Final_4_Hydrick_Server as server
import Final_4_Hydrick_Client1 as client1
import Final_4_Hydrick_Client2 as client2


if __name__ == "__main__":
    
    # create 2 threads to start the server and client
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=client1.start_client)
    t3 = threading.Thread(target=client2.start_client)

    # start the threads
    t1.start()
    t2.start()
    t3.start()