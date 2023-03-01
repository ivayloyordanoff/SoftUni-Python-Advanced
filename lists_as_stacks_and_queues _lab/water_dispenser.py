from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break

    queue.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{water_quantity} liters left")
        break

    elif "refill" in command:
        refill = command.split(" ")
        water_quantity += int(refill[1])

    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
