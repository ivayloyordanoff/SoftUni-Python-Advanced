rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

sum_of_matrix = 0

for i in range(len(matrix)):
    sum_of_matrix += sum(matrix[i])

print(sum_of_matrix)
print(matrix)
