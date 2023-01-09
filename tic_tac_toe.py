import random
import time


def init_board():
    """Initiate the board."""
    board = []
    for i in range(3):
        row = []
        board.append(row)
        for j in range(3):
            row.append('.')
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = 0
    col = 0
    is_input_valid = False
    while not is_input_valid:
        move = input(f"Please enter a move player {player}: ").upper()
        if move == "QUIT":
            print("It was nice playing with you. Goodbye.")
            quit()
        if len(move) != 2:
            print("Try again, enter a two character string")
        elif move[0] not in ("A", "B", "C"):
            print("Try again, the first character has to be 'A', 'B' or 'C'")
        elif move[1] not in ("1", "2", "3"):
            print("Try again, the second character has to be '1', '2'  or '3'")
        else:
            is_input_valid = True

    row = ('A', 'B', 'C').index(move[0])
    col = ('1', '2', '3').index(move[1])
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for AI on board."""
    row = 0
    col = 0

    is_free = True
    while is_free:
        row = random.choice(range(3))
        col = random.choice(range(3))
        if board[row][col] == ".":
            is_free = False
        if easy_win(board, player):
            row, col = easy_win(board, player)
        elif prevent_lose(board, player):
            row, col = prevent_lose(board, player)

    if is_full(board):
        return None
    else:
        return row, col


def easy_win(board, player):
    row = 0
    col = 0
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]
    columns = []
    for i in range(3):
        col = board[0][i], board[1][i], board[2][i]
        columns.append(col)
    if diagonal_1.count(player) == 2 and diagonal_1.count(".") == 1:
        row = diagonal_1.index(".")
        col = diagonal_1.index(".")
        return row, col
    if diagonal_2.count(player) == 2 and diagonal_2.count(".") == 1:
        row = diagonal_2.index(".")
        col = abs(diagonal_2.index(".") - 2)
        return row, col
    for i in range(3):
        if board[i].count(player) == 2 and board[i].count('.') == 1:
            row = i
            col = board[i].index('.')
            return row, col
        elif columns[i].count(player) == 2 and columns[i].count('.') == 1:
            col = i
            row = columns[i].index('.')
            return row, col


def prevent_lose(board, player):
    if player == 'X':
        player = '0'
    else:
        player = 'X'
    if easy_win(board, player):
        row, col = easy_win(board, player)
        return row, col


def mark(board, player, mode, row, col):
    """Marks the element at row & col on the board for player."""
    if mode == "AI-AI":
        row, col = get_ai_move(board, player)

    if board[row][col] == ".":
        board[row][col] = player
    else:
        print("This position is already taken.")
        row, col = get_move(board, player)
        mark(board, player, mode, row, col)


def print_board(initial_board):
    """Show the board."""
    rows = " A B C"
    board = ""
    for i in range(6):
        index = i // 2
        if i == 0:
            print("  1   2   3", end="")
        elif i % 2 != 0:
            board += (rows[i] + f" {initial_board[index][0]} | {initial_board[index][1]} | {initial_board[index][2]} ")
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
        print(f"{winner} has won!")
    else:
        print("It's a tie!")


def is_game_over(board, player, mode, row, col):
    """Marks the player move and shows who the winner is or if the board is full."""
    mark(board, player, mode, row, col)
    print_board(board)
    if has_won(board, player):
        print_result(player)
        return True
    elif is_full(board):
        player = 0
        print_result(player)
        return True
    else:
        return False


def tictactoe_game(mode='HUMAN-HUMAN'):
    """This is the game sequence depending on the game mode."""
    board = init_board()
    print_board(board)
    player = '0'
    while True:
        if mode == "AI-HUMAN":
            player = 'X'
            row, col = get_ai_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break
            player = '0'
            row, col = get_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break
        elif mode == "HUMAN-HUMAN":
            if player == "X":
                player = "0"
            else:
                player = "X"
            row, col = get_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break
        elif mode == "HUMAN-AI":
            player = 'X'
            row, col = get_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break
            player = '0'
            row, col = get_ai_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break
        elif mode == "AI-AI":
            time.sleep(1)
            if player == "X":
                player = "0"
            else:
                player = "X"
            row, col = get_ai_move(board, player)
            if is_game_over(board, player, mode, row, col):
                break


def main_menu():
    """Shows the start menu, where the user can choose the game mode."""
    is_mode_valid = False
    print(" ______   __     ______        ______   ______     ______        ______   ______     ______   ") 
    print("/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\  ") 
    print("\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\  ") 
    print("   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ ") 
    print("    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/") 
    print("")                                                                                               
    print(" __  __     ______     __  __     ______")                                                 
    print("/\_\_\_\   /\  __ \   /\_\_\_\   /\  __ \ ")
    print("\/_/\_\/_  \ \ \/\ \  \/_/\_\/_  \ \ \/\ \ ")
    print("  /\_\/\_\  \ \_____\   /\_\/\_\  \ \_____\ ")
    print("  \/_/\/_/   \/_____/   \/_/\/_/   \/_____/  ")
    print("")
    while not is_mode_valid:
        choice = input("Please choose the game mode: \n1 (HUMAN-HUMAN) \n2 (AI-HUMAN) \n3 (HUMAN-AI) \n4 (AI-AI)"
                       "\nYour choice: ")
        if choice == "1":
            is_mode_valid = True
            tictactoe_game("HUMAN-HUMAN")
        elif choice == "2":
            is_mode_valid = True
            tictactoe_game("AI-HUMAN")
        elif choice == "3":
            is_mode_valid = True
            tictactoe_game("HUMAN-AI")
        elif choice == "4":
            is_mode_valid = True
            tictactoe_game("AI-AI")
        else:
            print("Please choose 1, 2, 3 or 4 as game mode: ")


if __name__ == '__main__':
    main_menu()
