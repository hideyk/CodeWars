def validSolution(board):
    if any(0 in row for row in board):
        return False
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
    for j in range(9):
        set_vertical = set()
        for k in range(9):
            set_vertical.add(board[k][j])
        if len(set_vertical) != 9:
            return False
    for m in range(3):
        for n in range(3):
            set_cluster = set()
            set_cluster.add(board[3*m][3*n])
            set_cluster.add(board[3*m+1][3*n])
            set_cluster.add(board[3*m+2][3*n])
            set_cluster.add(board[3*m][3*n+1])
            set_cluster.add(board[3*m+1][3*n+1])
            set_cluster.add(board[3*m+2][3*n+1])
            set_cluster.add(board[3*m][3*n+2])
            set_cluster.add(board[3*m+1][3*n+2])
            set_cluster.add(board[3*m+2][3*n+2])
            if len(set_cluster) != 9:
                return False
    return True


def validSolution2(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows


def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            if not check_one_to_nine(nums):
                return False
    return True


def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True


def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True


def check_one_to_nine(lst):
    check = range(1, 10)
    return sorted(lst) == check


sudoku_board = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
# sudoku_board = [
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]

is_valid_solution = validSolution(sudoku_board)
print(is_valid_solution)