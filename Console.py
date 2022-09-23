"Console or terminal helper functions"
import os

class Console:
    "Console actions"
    @staticmethod
    def clear():
        "clear all commands from the console window"
        if os.name  in ('nt', 'dos'):
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)
        