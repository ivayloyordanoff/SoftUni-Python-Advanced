size = 6
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rover_pos = []
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for row in range(size):
    matrix.append(input().split())

    if "E" in matrix[row]:
        rover_pos = [row, matrix[row].index("E")]

commands = input().split(", ")

for command in commands:
    rover_pos = [
        rover_pos[0] + directions[command][0],
        rover_pos[1] + directions[command][1],
    ]

    if rover_pos[0] < 0:
        rover_pos[0] = size - 1
    elif rover_pos[0] == size:
        rover_pos[0] = 0
    elif rover_pos[1] < 0:
        rover_pos[1] = size - 1
    elif rover_pos[1] == size:
        rover_pos[1] = 0

    if matrix[rover_pos[0]][rover_pos[1]] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    elif matrix[rover_pos[0]][rover_pos[1]] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    elif matrix[rover_pos[0]][rover_pos[1]] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    elif matrix[rover_pos[0]][rover_pos[1]] == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
