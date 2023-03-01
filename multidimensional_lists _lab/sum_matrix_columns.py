rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = []

for i in range(cols):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]
    result.append(col_sum)

[print(x) for x in result]
