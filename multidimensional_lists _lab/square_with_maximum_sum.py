rows, cols = [int(x) for x in input().split(", ")]
matrix = []
submatrix = []
biggest_sum = 0

for row in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

for row in range(len(matrix) - 1):
    for col in range(cols - 1):
        first_row = matrix[row][col], matrix[row][col + 1]
        second_row = matrix[row + 1][col], matrix[row + 1][col + 1]
        current_sum = sum(first_row + second_row)
        if current_sum > biggest_sum:
            submatrix.clear()
            submatrix.append(first_row)
            submatrix.append(second_row)
            biggest_sum = current_sum

[print(*submatrix[row]) for row in range(2)]
print(biggest_sum)
