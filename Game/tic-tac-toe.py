# tic_tac_toe.py

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter row (0, 1, 2): "))
        col = int(input(f"Player {players[current_player]}, enter col (0, 1, 2): "))

        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    main()
