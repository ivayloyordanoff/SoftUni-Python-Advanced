from collections import deque

seats = input().split(", ")
first_numbers = deque(int(x) for x in input().split(","))
second_numbers = deque(int(x) for x in input().split(","))

seat_matches = []
rotations = 0

while len(seat_matches) < 3:
    if rotations == 10:
        break

    first_number = first_numbers.popleft()
    second_number = second_numbers.pop()

    current_sum = first_number + second_number
    char = chr(current_sum)

    first_comb = str(first_number) + char
    second_comb = str(second_number) + char

    if first_comb in seats and first_comb not in seat_matches:
        seat_matches.append(first_comb)
    elif second_comb in seats and second_comb not in seat_matches:
        seat_matches.append(second_comb)
    else:
        first_numbers.append(first_number)
        second_numbers.appendleft(second_number)

    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
