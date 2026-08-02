board = [" " for _ in range(9)]
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
def check_win(player):
    win_cond = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_cond)
print("--- Tic-Tac-Toe ---")
current_player = "X"
for turn in range(9):
    print_board()
    try:
        move = int(input(f"Player {current_player}, enter move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! You lose a turn.")
    except ValueError:
        print("Enter a number!")
else:
    print_board()
    print("It's a tie!")
# Game Over
print("Thanks for playing!")
# End of code