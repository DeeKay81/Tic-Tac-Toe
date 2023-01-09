def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append('.')
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    player = "X"
    row = 0
    col = 0
    is_input_valid = False
    get_move = ""
    while not is_input_valid:
        get_move = input(f"Please enter a move player {player}: ")
        print("this is a loop")
        if get_move != 2:
            print("try again idiot")
            is_input_valid = False
            continue
        if get_move[0] not in ("A", "B", "C"):
            print("try again idiot")
            is_input_valid = False
            continue
        if get_move[1] not in ("1", "2", "3"):
            print("try again idiot")
            is_input_valid = False
        else:
            is_input_valid = True
        #is_input_valid = False

        # this is for the rows
    if get_move[0] == "A":
        row = 0
    elif get_move[0] == "B":
        row = 1
    elif get_move[0] == "C":
        row = 2
    # this is for the colums
    if get_move[1] == "1":
        col = 0
    elif get_move[1] == "2":
        col = 1
    elif get_move[1] == "3":
        col = 2
    print(row, col)
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player

    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


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
            board += rows[i] + \
                f" {initial_board[index][0]} | {initial_board[index][1]} | {initial_board[index][2]} "
        else:
            board += " ---+---+---"
        # don't forget to start a new line after each row using "\n"
        board += "\n"
    print(board)


initial_board = init_board()
print_board(initial_board)

get_move(initial_board, player="X")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
#    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
