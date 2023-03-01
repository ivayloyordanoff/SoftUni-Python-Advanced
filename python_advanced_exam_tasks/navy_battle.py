size = int(input())

battlefield = []
submarine_pos = []
mine_hits = 0
cruisers_destroyed = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        submarine_pos = [row, battlefield[row].index("S")]
        battlefield[row][submarine_pos[1]] = "-"

while True:
    command = input()

    if command not in directions:
        continue

    current_pos = [
        submarine_pos[0] + directions[command][0],
        submarine_pos[1] + directions[command][1],
        ]

    if not (0 <= current_pos[0] < size and 0 <= current_pos[1] < size):
        continue

    if battlefield[current_pos[0]][current_pos[1]] == "*":
        mine_hits += 1

        if mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates {current_pos}!")
            battlefield[current_pos[0]][current_pos[1]] = "S"
            [print("".join(row)) for row in battlefield]
            break

        else:
            battlefield[current_pos[0]][current_pos[1]] = "-"

    elif battlefield[current_pos[0]][current_pos[1]] == "C":
        cruisers_destroyed += 1

        if cruisers_destroyed == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[current_pos[0]][current_pos[1]] = "S"
            [print("".join(row)) for row in battlefield]
            break

        else:
            battlefield[current_pos[0]][current_pos[1]] = "-"
    submarine_pos = current_pos
