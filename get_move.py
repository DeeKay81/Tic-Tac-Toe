def init_board():
    board = []
    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append('.')
    return board

def get_move(board, player):
    player = "X"
    row = 0
    col = 0
    is_input_valid = False
    #get_move = ""
    while not is_input_valid:
        get_move = input(f"Please enter a move player {player}: ").upper()
        print(get_move)
        if len(get_move) != 2:
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

def has_won(board, player):
    for a in board:
        if a[0] == player and a[1] == player and a[2] == player:
            
        


def print_board(initial_board):
    rows = " A B C"
    board = ""
    for i in range(6):
        index = i // 2
        if i == 0:
            print("  1   2   3", end="")
        elif i % 2 != 0:
            board += rows[i] + f" {initial_board[index][0]} | {initial_board[index][1]} | {initial_board[index][2]} "
        else:
            board += " ---+---+---"
        board += "\n"
    print(board)

initial_board = init_board()
print_board(initial_board)

get_move(initial_board, player= "X")
