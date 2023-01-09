def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append('.')
    
    print(board)
    return board



initial_board = init_board()
initial_board[0][1] = 'X'
def print_board(initial_board):
    """Prints a 3-by-3 board on the screen with borders."""
    rows = " A B C"
    board = ""
    # there are 5 rows in a standard tic-tac-toe board
    for i in range(6):
        index = i // 2
        # switch between printing vertical and horizontal bars
        if i == 0:
            print("  1   2   3", end="")
        elif i % 2 != 0:
            board += rows[i] + f" {initial_board[index][0]} | {initial_board[index][1]} | {initial_board[index][2]} "
        else:
            board += " ---+---+---"
        # don't forget to start a new line after each row using "\n"
        board += "\n"
    print(board)


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    move_str = input(f"Player {player}, enter your move: ")
    #row, col = 0, 0
    if is_input_valid(input):
        try:
            row = int(move_str[0])
            col = int(move_str[1])

        except ValueError:
            print("Please, enter a valid move")
        return row, col
    else:
        print(f"{move_str} is not a valid move.")

def is_input_valid(input):
    if input.lower() == "quit":
        return True
    if len(input) == 2:
        if input[0] in ['a', 'b', 'c'] and input[1] in [1, 2, 3]:
            return True
    return False



print_board(initial_board)
