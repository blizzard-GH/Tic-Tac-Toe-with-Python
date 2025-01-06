def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
        return False

def play_game():
    board = [" "] * 9
    current_player = "X"

    for turn in range(9):
        display_board(board)
        move = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
        if board[move] != " ":
            print("Position already taken. Try Again.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations, player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    play_game()