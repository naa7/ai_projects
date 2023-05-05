'''

a) To generate a "smart" search tree, we can use the concept of backtracking.
    We can start by placing a queen in the first row, then move to the second
    row and place a queen in a column that does not conflict with the queen in
    the first row. We continue this process for each row, backtracking if we
    reach a dead end. This approach significantly reduces the number of possible
    placements that need to be considered.

b) We can use a 2D list to represent the chess board, where each element is
    either 0 or 1. We can also use a list to keep track of the positions of
    then queens.

c) The best loop structure to use is a for loop, as we know exactly how many
    queens we need to place and in which row.

d) Code below

'''

def is_valid(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the same diagonal (upper left)
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the same diagonal (upper right)
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0

    return False

board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(0)
    board.append(row)

# Solve the problem
if solve(board, 0):
    # Print the solution
    for row in board:
        print(row)
else:
    print("No solution found.")