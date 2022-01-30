import os
import numpy as np

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') or None # function to clear interpreter terminal.

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

TRIGGERED = "XX"

def isWin(my_array):
    output = False
    for i in range(4):
        if np.all(my_array[:,i]==TRIGGERED):
            output = True
            break
    if not output:
        for i in range(4):
            if np.all(my_array[i,:]==TRIGGERED):
                output = True
                break
    if not output:
        if np.all(np.diag(my_array)==TRIGGERED):
            output = True
    if not output:
        if np.all(np.diag(np.fliplr(my_array))==TRIGGERED):
            output = True
    return output
