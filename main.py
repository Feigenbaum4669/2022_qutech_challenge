import Auxilliary_functions_Bingo.helper_functions as hf
import Auxilliary_functions_Bingo.quantum_backend as qb

if __name__ == '__main__':
    hf.clear()
    default_valid_inputs = ['I', 'X0', 'X1', 'X2', 'X3', 'X4', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Z0', 'Z1', 'Z2', 'Z3',
                            'Z4']
    valid_inputs = default_valid_inputs
    backend = qb.get_QI_backend(backend_type="QX single-node simulator")

    board_1 = hf.initialize_board()
    board_2 = hf.initialize_board()

    while True:

        while True:
            hf.print_boards([board_1])

            input_error = input("\nPlayer 1 - Please insert single-qubit error: ")
            hf.clear()
            if input_error not in valid_inputs:
                print("Wrong move. Please enter valid inputs only. ")
            else:
                print("Running circuit on Quantum-Inspire...")
                valid_inputs.remove(input_error)
                break
        move = hf.get_error_syndrome(input_error, backend)

        hf.update_board(board_1, move)
        hf.update_board(board_2, move)

        input_error = hf.silly_bot(valid_inputs)

        print("Running circuit on Quantum-Inspire...")
        valid_inputs.remove(input_error)

        move = hf.get_error_syndrome(input_error, backend)

        hf.update_board(board_1, move)
        hf.update_board(board_2, move)

        player_1_wins = hf.isWin(board_1)
        player_2_wins = hf.isWin(board_2)

        if player_1_wins and player_2_wins:
            hf.print_boards([board_1, board_2])
            print(f"\n🎉🥳 {hf.OKCYAN}Tie! Maybe try again?{hf.ENDC} 🎉🥳")
            break
        elif player_1_wins:
            hf.print_boards([board_1, board_2])
            print(f"\n🎉🥳 {hf.OKGREEN}You won! Congratulations!{hf.ENDC} 🎉🥳")
            break
        elif player_2_wins:
            hf.print_boards([board_1, board_2])
            print(f"\n🎉🥳 {hf.FAIL}You lose. Maybe try again?{hf.ENDC} 🎉🥳")
            break
