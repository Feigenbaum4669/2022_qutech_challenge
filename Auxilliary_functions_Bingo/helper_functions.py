import os
import random
import numpy as np
import pandas as pd

import quantum_backend as qb

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') or None  # function to clear interpreter terminal.

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
        if np.all(my_array[:, i] == TRIGGERED):
            output = True
            break
    if not output:
        for i in range(4):
            if np.all(my_array[i, :] == TRIGGERED):
                output = True
                break
    if not output:
        if np.all(np.diag(my_array) == TRIGGERED):
            output = True
    if not output:
        if np.all(np.diag(np.fliplr(my_array)) == TRIGGERED):
            output = True
    return output


def get_error_syndrome_fake(input):
    fake_error_syndrome = {'I': 0, 'X0': 1, 'X1': 2, 'X2': 3, 'X3': 4, 'X4': 5, 'Y0': 6, 'Y1': 7, 'Y2': 8, 'Y3': 9,
                           'Y4': 10, 'Z0': 11, 'Z1': 12, 'Z2': 13, 'Z3': 14, 'Z4': 15}
    return str(fake_error_syndrome[input])


def get_error_syndrome(input_error, backend):
    qc_job = qb.execute_QuantumCircuit(input_error, backend=backend, shots=256)
    result_dict = qc_job.result().get_counts()
    ans_bin = max(result_dict, key=result_dict.get)
    ans = str(int(ans_bin, 2))
    return ans


def initialize_board():
    my_array = np.array([str(i) for i in range(16)])
    np.random.shuffle(my_array)
    return my_array.reshape([4, 4])


def print_boards(boards):
    for index, board in enumerate(boards):
        print("Player " + str(index + 1) + " board:")
        df = pd.DataFrame(board)
        print(df.to_string(index=False, header=False))


def update_board(board, move):
    board[board == move] = TRIGGERED
    return board

def silly_bot(valid_inputs):
    random_move = random.choice(valid_inputs)
    print("\nBot is chosing: "+random_move)
    return random_move
