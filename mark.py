def init_board():
    board = []
    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append('.')
    return board


def get_move(board, player):
    row = 0
    col = 0
    is_input_valid = False
    while not is_input_valid:
        get_move = input(f"Please enter a move player {player}: ").upper()
        print(get_move)
        if len(get_move) != 2:
            print("try again idiot")
            is_input_valid = False
            continue
        if get_move[0] not in ("A", "B", "C"):
            print("not str")
            is_input_valid = False
            continue
        if get_move[1] not in ("1", "2", "3"):
            print("not int")
            is_input_valid = False
            continue
        is_input_valid = True

        # this is for the rows
    if get_move[0] == "A":
        row = 0
    elif get_move[0] == "B":
        row = 1
    elif get_move[0] == "C":
        row = 2
    # this is for the columns
    if get_move[1] == "1":
        col = 0
    elif get_move[1] == "2":
        col = 1
    elif get_move[1] == "3":
        col = 2
    print(row, col)
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == ".":
        board[row][col] = player
    else:
        row, col = get_move(board, player)
        mark(board, player, row, col)
        


def print_board(initial_board):
    rows = " A B C"
    board = ""
    for i in range(6):
        index = i // 2
        if i == 0:
            print("  1   2   3", end="")
        elif i % 2 != 0:
            board += rows[i] + \
                f" {initial_board[index][0]} | {initial_board[index][1]} | {initial_board[index][2]} "
        else:
            board += " ---+---+---"
        board += "\n"
    print(board)


initial_board = init_board()
print_board(initial_board)


def tictactoe_game(mode='HUMAN-HUMAN'):
    player = "0"
    while True:
        if player == "X":
            player = "0"
        else:
            player = "X"
        row, col = get_move(initial_board, player)
        mark(initial_board, player, row, col)
        print_board(initial_board)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
