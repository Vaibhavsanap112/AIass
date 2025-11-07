
import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print("-" * 5)

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == "X":
                return 10
            elif board[row][0] == "O":
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return 10
            elif board[0][col] == "O":
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 10
        elif board[0][0] == "O":
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 10
        elif board[0][2] == "O":
            return -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

if __name__ == "__main__":
    board = [
        ["X", "O", "X"],
        ["O", "X", " "],
        [" ", " ", "O"]
    ]

    print("Current Board:")
    print_board(board)

    best_move = find_best_move(board)

    print(f"\nThe best move for X is: Row = {best_move[0]}, Column = {best_move[1]}")
    Prints the 3×3 Tic Tac Toe board.

#The board b is a list of 9 items ("X", "O", or " ").

It prints 3 symbols per line (0–2, 3–5, 6–8).

The last print() just adds a blank line for spacing.

🏆 2. winner(b, p)
def winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in wins)


Defines all 8 possible winning lines (rows, columns, diagonals).

Checks if all three positions in any line have the same symbol p.

Returns True if that player wins, else False.

🧠 3. minimax(b, is_max)
def minimax(b, is_max):
    if winner(b,"O"): return 1
    if winner(b,"X"): return -1
    if " " not in b: return 0


This is the AI’s decision-making function.

Base cases:

If O (computer) wins → score +1

If X (player) wins → score -1

If no empty spaces → score 0 (draw)

🤖 4. Computer’s turn (maximize score)
    if is_max:
        best = -2
        for i in range(9):
            if b[i]==" ":
                b[i]="O"
                best = max(best, minimax(b, False))
                b[i]=" "
        return best


When it’s the computer’s turn, it tries all empty spots.

It places "O" temporarily and calls minimax again assuming the next turn is the player’s (False).

After checking, it undoes the move (b[i] = " ").

Keeps the highest score (best move for computer).

🧍‍♂️ 5. Player’s turn (minimize score)
    else:
        best = 2
        for i in range(9):
            if b[i]==" ":
                b[i]="X"
                best = min(best, minimax(b, True))
                b[i]=" "
        return best


When it’s the player’s turn, it also tries all empty spots.

It assumes the player will play optimally to minimize the computer’s score.

Keeps the lowest score (worst for computer, best for player).

🎯 6. Finding the best move
def best_move(b):
    best, move = -2, -1
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            score = minimax(b, False)
            b[i]=" "
            if score > best:
                best, move = score, i
    return move


Loops through all empty spots.

For each possible computer move, calls minimax to get its score.

Chooses the move with the highest score.

🕹️ 7. Main game loop
board = [" "]*9
print("You are X, computer is O (enter 0-8):")
print_board(board)


Creates an empty board of 9 spaces.

Displays instructions and the empty grid.

👤 Player’s move
p = int(input("Your move: "))
if board[p]!=" ":
    print("Invalid!"); continue
board[p]="X"
print_board(board)
if winner(board,"X"): print("You win!"); break
if " " not in board: print("Draw!"); break


Asks for player input (0–8).

Checks if the chosen cell is free.

Places "X" and prints the board.

Checks if the player has won or if it’s a draw.

💻 Computer’s move
c = best_move(board)
board[c]="O"
print("Computer:", c)
print_board(board)
if winner(board,"O"): print("Computer wins!"); break
if " " not in board: print("Draw!"); break


Calls best_move() to pick the best possible spot.

Places "O" there and prints the board.

Checks for win or draw again.

🏁 Example Game Output
You are X, computer is O (enter 0-8):

Your move: 0
X
Computer: 4
X   O
Your move: 1
X X
Computer: 2
X X O
Computer: 6
Computer wins!
"""

