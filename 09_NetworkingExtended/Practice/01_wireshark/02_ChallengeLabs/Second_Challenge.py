"""
# Open challenge101-1.pcapng and answer these Challenge questions.

Important: This trace file includes an HTTP communication running over a non-standard port number. 
Before you can answer these questions, you must force wireshark to dissect this traffic as HTTP.

Q1: In which frame number does the client request the default web page("/")?
A: 13

Q2: What response code does the server send in frame 17?
A: 200 OK

Q3: What is the largest TCP delta value seen in this trace file?
A: Frame 7, Delta: 22.84

Q4: How many SYN packets arrived after at least a 1 second delay?
A: 4
"""