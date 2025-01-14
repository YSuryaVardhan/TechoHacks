def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, mark):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == mark for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter col (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("The game is a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
