#THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
#A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - YUNNIE YU

import random

# Function for printing the game board
def print_board(board):
    count = 0
    for row in board:
        row_str = []
        for cell in row:
            row_str.append(cell if cell != ' ' else "-") # append the content or leave it blank
            count += 1
        print(' | '.join(row_str))
    print("\n")

# Function for check whether the game is win or lose or draw
# and will return True for wining the game and name of the winner
def is_end_state(board):
    # check the row for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True, row[0]
    # check the col for winner
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True, board[0][col]
    # check the diagonal for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True, board[0][2]
    # check for the draw
    for row in board:
        for cell in row:
            if cell == ' ':
                return False, ''
    return True, 'D'

# Function for calculating the utility of the game board
# and will return the utility
def utility(board):
    _, winner = is_end_state(board) # state of the game and name of the winner
    A = 0
    # the computer is the maximizer
    if winner == 'X':
        A = 1
    # the user is the minimizer
    elif winner == 'O':
        A = -1
    # calculate the utility use the formula provided
    B = sum(row.count(' ') for row in board) + 1
    return A * B # return the utility

# Function for minimax algorithm for the computer to find the optimal solution
def minimax(board, depth, maximizing_player):
    end_state, winner = is_end_state(board)
    # if the game is over, return the result
    if end_state:
        return utility(board)

    # else keep on going
    # Computer's turn
    if maximizing_player:
        max_eval = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    # User's turn
    else:
        min_eval = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function for computer to find the optimal choice
def computer_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Function for playing the game
def tic_tac_toe():
    # initialize the empty game board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    # Computer goes first
    i, j = random.choice([(x, y) for x in range(3) for y in range(3)]) # randomly select a position
    board[i][j] = 'X'
    print_board(board)
    
    while True:
        # check the state first
        end_state, winner = is_end_state(board) 
        if end_state:
            if winner == 'D':
                print("It's a Draw!")
            else:
                print(f"{winner} wins!")
            break
        # for user to input
        while True:
            user_move = input("Enter your move (0-8): ")
            # solution for invalid input
            if not user_move.isdigit() or int(user_move) < 0 or int(user_move) > 8:
                print("Invalid input! Please enter a number between 0 and 8.")
                continue
            # a tuple containing the quotient and the remainder when dividing a by b.
            i, j = divmod(int(user_move), 3)
            # solution for selecting the occupied position
            if board[i][j] != ' ':
                print("Invalid move! The cell is already occupied.")
                continue
            break
        board[i][j] = 'O' # user's choice
        print_board(board)
        # check the state of the game everytime after one's turns
        end_state, winner = is_end_state(board)
        if end_state:
            if winner == 'D':
                print("It's a Draw!")
            else:
                print(f"{winner} wins!")
            break
        
        # Computer makes the optimal move for subsequent turns
        i, j = computer_move(board)
        board[i][j] = 'X'
        print_board(board)

# Play the game!!!
if __name__ == "__main__":
    tic_tac_toe()
