def is_valid(board, row, col, num):
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in map(str, range(1, 10)):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = '0'

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                return (i, j)
    return None

sudoku_grid = [
    "800000000",
    "003600000",
    "070090200",
    "050007000",
    "000045700",
    "000100030",
    "001000068",
    "008500010",
    "090000400"
]

sudoku_grid = [list(row) for row in sudoku_grid]

if solve_sudoku(sudoku_grid):
    print("Sudoku solution:")
    for row in sudoku_grid:
        print("".join(row))
else:
    print("No solution exists.")

#END OF CODE
#COPY MAT KARNA NA PLEASE, UMMMM...... NHI NHI COPY KARLENA PAR EK BAAR BATA DENA CONNECT KARKE IF YOU WISH TO PLEASE PLEASE, THIS IS THE LEAST I CAN EXPECT!
