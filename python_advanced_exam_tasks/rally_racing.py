size = int(input())
racing_number = input()

matrix = []
car_pos = [0, 0]

tunnel_pos = []
distance_covered = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "T" in matrix[row]:
        tunnel_pos.append((row, matrix[row].index("T")))

while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    car_pos = [
        car_pos[0] + directions[command][0],
        car_pos[1] + directions[command][1],
    ]

    if 0 <= car_pos[0] < size and 0 <= car_pos[1] < size:
        if matrix[car_pos[0]][car_pos[1]] == ".":
            distance_covered += 10

        if matrix[car_pos[0]][car_pos[1]] == "T":
            distance_covered += 30
            matrix[car_pos[0]][car_pos[1]] = "."
            tunnel_pos.remove(tunnel_pos[0])
            car_pos = tunnel_pos[0]
            matrix[car_pos[0]][car_pos[1]] = "."

        if matrix[car_pos[0]][car_pos[1]] == "F":
            distance_covered += 10
            matrix[car_pos[0]][car_pos[1]] = "C"
            print(f"Racing car {racing_number} finished the stage!")
            break

matrix[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {distance_covered} km.")
[print(*row, sep="") for row in matrix]
