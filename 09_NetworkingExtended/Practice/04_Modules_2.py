"""
2. Write a script that runs a command and captures the 
    number of bytes in a print statement.
"""

# import needed libraries
import subprocess, os

command_to_run = input("Please enter the command you would like run: ")

# function that runs a command that is passed to it as an argument
def run_command(command):

        output = subprocess.check_output(command, shell=True)
        return output

cmd_output = run_command(command_to_run)
print(f"Output is {len(cmd_output)} bytes long.")