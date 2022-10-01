"Console or terminal helper functions"
import os

def clear():
    "clear all commands from the console window"
    if os.name  in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)