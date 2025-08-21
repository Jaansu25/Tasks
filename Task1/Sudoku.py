def solveSudoku(board):
    def is_valid(r, c, num):
        # check row
        for i in range(9):
            if board[r][i] == num:
                return False
        # check column
        for i in range(9):
            if board[i][c] == num:
                return False
        # check 3x3 sub-box
        startRow, startCol = 3 * (r // 3), 3 * (c // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # empty cell
                    for num in map(str, range(1, 10)):
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = "."  # undo (backtrack)
                    return False  # no valid number
        return True  # solved
    backtrack()

board = []
for _ in range(9):
    row = list(input().strip())  # take input as string and convert to list
    if len(row) != 9:
        exit()
    board.append(row)

solveSudoku(board)

for row in board:
    print(" ".join(row))