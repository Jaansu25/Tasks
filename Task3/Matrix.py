import ast

def maximalRectangle(matrix):
    
    max_area = 0
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                width = float('inf')
                for k in range(i, rows):
                    if matrix[k][j] == '0':
                        break
                    current_width = 0
                    while current_width + j < cols and matrix[k][j + current_width] == '1':
                        current_width += 1
                    width = min(width, current_width)
                    max_area = max(max_area, width * (k - i + 1))
    return max_area

matrix_input = input()
matrix = ast.literal_eval(matrix_input)  # safely evaluate the input

print(maximalRectangle(matrix))