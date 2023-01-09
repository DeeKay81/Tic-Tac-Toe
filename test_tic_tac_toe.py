import random


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
        move = input(f"Please enter a move player {player}: ").upper()
        if move == "QUIT":
            print("It was nice playing with you. Good bye.")
            quit()
        if len(move) != 2:
            print("Try again idiot, enter a two character string")
        elif move[0] not in ("A", "B", "C"):
            print("Try again, the first character has to be 'A', 'B' or 'C'")
        elif move[1] not in ("1", "2", "3"):
            print("Try again, the second character has to be '1', '2'  or '3'")
        else:
            is_input_valid = True

    row = ('A', 'B', 'C').index(move[0])
    col = ('1', '2', '3').index(move[1])

    #if get_move[0] == "A":
    #    row = 0
    # elif get_move[0] == "B":
    #     row = 1
    # elif get_move[0] == "C":
    #     row = 2
    # this is for the columns
    # if get_move[1] == "1":
    #     col = 0
    # elif get_move[1] == "2":
    #     col = 1
    # elif get_move[1] == "3":
    #     col = 2
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""

    row = 0
    col = 0

    columns = []
    for i in range(3):
        col = board[0][i], board[1][i], board[2][i]
        columns.append(col)

    is_free = True
    while is_free:
        row = random.choice(range(3))
        col = random.choice(range(3))
        if board[row][col] == ".":
            is_free = False

        for i in range(3):
            if board[i].count(player) == 2 and board[i].count('.') == 1:
                row = i
                col = board[i].index('.')
                return row, col
            if columns[i].count(player) == 2 and columns[i].count('.') == 1:
                col = i
                row = columns[i].index('.')

    if is_full(board):
        return None
    else:
        return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == ".":
        board[row][col] = player
    else:
        print("This place is already taken.")
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


def is_full(board):
    """Returns True if board is full."""
    for a in board:
        for b in a:
            if b == ".":
                return False
    return True


def has_won(board, player):
    """Returns True if player has won the game."""
    #for a in board:
    #     if a[0] == player and a[1] == player and a[2] == player:
    #         return True
    # if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    #     return True
    # elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
    #     return True
    # elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
    #     return True
    # elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
    #     return True
    # elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
    #     return True
    # else:
    #     return False

    for i in range(3):
        if ((board[i][0] == board[i][1] == board[i][2] == player) or
           (board[0][i] == board[1][i] == board[2][i] == player)):
            return True
        if ((board[0][0] == board[1][1] == board[2][2] == player) or
           (board[0][2] == board[1][1] == board[2][0] == player)):
            return True
    return False


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner:
        print(f"Player {winner}, you have won!")
    else:
        print("It's a tie!")


def end_game(board, player):
    if has_won(board, player):
        print_result(player)
        return True
    if is_full(board):
        player = 0
        print_result(player)
        return True


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    print_board(board)
    player = '0'

    while True:

        if mode == ("AI-HUMAN"):
            player = 'X'
            row, col = get_ai_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if end_game(board, player):
                break
            player = '0'
            row, col = get_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if end_game(board, player):
                break

        elif mode == "HUMAN-HUMAN":
            if player == "X":
                player = "0"
            else:
                player = "X"
            row, col = get_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if end_game(board, player):
                break

        elif mode == "HUMAN-AI":
            player = 'X'
            row, col = get_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if end_game(board, player):
                break
            player = '0'
            row, col = get_ai_move(board, player)
            mark(board, player, row, col)
            print_board(board)
            if end_game(board, player):
                break


def main_menu():
    choice = input(
        "Please choose the game mode: 1 (HUMAN-HUMAN), 2 (AI-HUMAN), 3 (HUMAN-AI): ")
    if choice == '1':
        tictactoe_game("HUMAN-HUMAN")
    elif choice == '2':
        tictactoe_game("AI-HUMAN")
    elif choice == "3":
        tictactoe_game("HUMAN-AI")


if __name__ == '__main__':
    main_menu()
