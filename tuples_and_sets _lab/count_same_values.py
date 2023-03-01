numbers = tuple(map(float, input().split()))
numbers_counter = {}

for num in numbers:
    if num not in numbers_counter:
        numbers_counter[num] = 0
    numbers_counter[num] += 1

[print(f"{key} - {value} times") for key, value in numbers_counter.items()]
