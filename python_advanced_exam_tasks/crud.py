size = 6
matrix = [input().split() for _ in range(size)]
pos_as_string = input()
pos = [int(pos_as_string[1]), int(pos_as_string[4])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    if command[0] == "Create":
        direction, value = command[1], command[2]

        pos = [
            pos[0] + directions[direction][0],
            pos[1] + directions[direction][1],
        ]

        if matrix[pos[0]][pos[1]] == ".":
            matrix[pos[0]][pos[1]] = value

    elif command[0] == "Update":
        direction, value = command[1], command[2]

        pos = [
            pos[0] + directions[direction][0],
            pos[1] + directions[direction][1],
        ]

        if matrix[pos[0]][pos[1]].isalnum():
            matrix[pos[0]][pos[1]] = value

    elif command[0] == "Delete":
        direction = command[1]

        pos = [
            pos[0] + directions[direction][0],
            pos[1] + directions[direction][1],
        ]

        if matrix[pos[0]][pos[1]].isalnum():
            matrix[pos[0]][pos[1]] = "."

    elif command[0] == "Read":
        direction = command[1]

        pos = [
            pos[0] + directions[direction][0],
            pos[1] + directions[direction][1],
        ]

        if matrix[pos[0]][pos[1]].isalnum():
            print(matrix[pos[0]][pos[1]])

[print(*row) for row in matrix]
