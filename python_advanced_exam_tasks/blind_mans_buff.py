rows, cols = [int(x) for x in input().split()]

playground = []
my_pos = []
touched_opponents = 0
moves_made = 0

for row in range(rows):
    playground.append(input().split())

    if "B" in playground[row]:
        my_pos = row, playground[row].index("B")
        playground[my_pos[0]][my_pos[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "Finish":
        break

    my_pos = [
        my_pos[0] + directions[command][0],
        my_pos[1] + directions[command][1],
    ]

    if not (0 <= my_pos[0] < rows and 0 <= my_pos[1] < cols):
        my_pos = [
            my_pos[0] - directions[command][0],
            my_pos[1] - directions[command][1],
        ]
        continue

    if playground[my_pos[0]][my_pos[1]] == "O":
        my_pos = [
            my_pos[0] - directions[command][0],
            my_pos[1] - directions[command][1],
        ]
        continue

    elif playground[my_pos[0]][my_pos[1]] == "-":
        moves_made += 1

    elif playground[my_pos[0]][my_pos[1]] == "P":
        touched_opponents += 1
        moves_made += 1
        playground[my_pos[0]][my_pos[1]] = "-"

        if touched_opponents == 3:
            break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
