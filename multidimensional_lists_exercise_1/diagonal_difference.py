n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[n - 1 - r][r] for r in range(n - 1, - 1, - 1)]

print(abs(sum(primary) - sum(secondary)))
