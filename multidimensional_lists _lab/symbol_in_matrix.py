matrix = [list(input()) for row in range(int(input()))]
symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix)):
        current_element = matrix[row][col]
        if current_element == symbol:
            print((row, col))
            raise SystemExit
print(f"{symbol} does not occur in the matrix")
