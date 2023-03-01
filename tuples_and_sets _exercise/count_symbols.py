occurrences = {}

for char in input():
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1

for key, value in sorted(occurrences.items()):
    print(f"{key}: {value} time/s")
