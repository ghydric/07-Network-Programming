"""
3. Write a script that runs a command to display your current directory.
"""

# import needed libraries
import subprocess, os

command_to_run = input("Please enter the command you would like run: ")
command_to_run = command_to_run.split(" ")

# function that runs a command that is passed to it as an argument
def run_command(command):

        x = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        return x.communicate(x.stdout)

cmd_output = run_command(command_to_run)
print(cmd_output)