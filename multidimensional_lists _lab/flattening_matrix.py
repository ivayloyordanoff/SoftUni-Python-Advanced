rows = int(input())

matrix = []

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

result = [num for row in matrix for num in row]
print(result)
