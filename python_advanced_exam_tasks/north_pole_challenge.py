rows, cols = map(int, input().split(", "))
field = []

my_pos = []
total_items = 0

collected_decorations = 0
collected_gifts = 0
collected_cookies = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    field.append(input().split())

    if "Y" in field[row]:
        my_pos = row, field[row].index("Y")
        field[my_pos[0]][my_pos[1]] = "x"

for row in field:
    for col in row:
        if "D" in col:
            total_items += 1

        if "G" in col:
            total_items += 1

        if "C" in col:
            total_items += 1

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    direction, steps = command[0], int(command[1])

    for _ in range(steps):
        my_pos = [
            my_pos[0] + directions[direction][0],
            my_pos[1] + directions[direction][1],
        ]

        if my_pos[0] < 0:
            my_pos[0] = rows - 1
        elif my_pos[0] == rows:
            my_pos[0] = 0
        elif my_pos[1] < 0:
            my_pos[1] = cols - 1
        elif my_pos[1] == cols:
            my_pos[1] = 0

        if field[my_pos[0]][my_pos[1]] == "D":
            collected_decorations += 1
        elif field[my_pos[0]][my_pos[1]] == "G":
            collected_gifts += 1
        elif field[my_pos[0]][my_pos[1]] == "C":
            collected_cookies += 1

        if collected_decorations + collected_gifts + collected_cookies == total_items:
            field[my_pos[0]][my_pos[1]] = "Y"
            print("Merry Christmas!")
            print(f"You've collected:\n- {collected_decorations} Christmas decorations\n\
- {collected_gifts} Gifts\n- {collected_cookies} Cookies")
            [print(*row) for row in field]
            raise SystemExit

        field[my_pos[0]][my_pos[1]] = "x"

field[my_pos[0]][my_pos[1]] = "Y"

print(f"You've collected:\n- {collected_decorations} Christmas decorations\n\
- {collected_gifts} Gifts\n- {collected_cookies} Cookies")
[print(*row) for row in field]
