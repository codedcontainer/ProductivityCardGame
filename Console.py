import os

class Console:
    @staticmethod
    def clear():
        if os.name  in ('nt', 'dos'):
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)
        