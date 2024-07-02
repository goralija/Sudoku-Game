def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not repeated in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not repeated in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
            
    return True

def solve_sudoku(board):
    empty_spot = find_empty(board)
    if not empty_spot:
        return True  # No empty spots, puzzle is solved
    row, col = empty_spot

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Reset if placing num didn't lead to solution

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:  # 0 means the cell is empty
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()
    
def make_validity_board(board):
    validity_board = []
    for row in board:
        valid_row = []
        for num in row:
            valid_row.append(num != 0)
        validity_board.append(valid_row)
    return validity_board