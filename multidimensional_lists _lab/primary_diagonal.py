size_of_matrix = int(input())

matrix = []

for i in range(size_of_matrix):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]

print(sum(primary_diagonal))
