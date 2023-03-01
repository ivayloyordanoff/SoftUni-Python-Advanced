from collections import deque

substrings = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

colors_list = []

while substrings:
    first_substring = substrings.popleft()
    last_substring = substrings.pop() if substrings else ''

    for color in (first_substring + last_substring, last_substring + first_substring):
        if color in colors:
            colors_list.append(color)
            break
    else:
        for el in (first_substring[:-1], last_substring[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)

for color in set(req_colors.keys()).intersection(colors_list):
    if not req_colors[color].issubset(colors_list):
        colors_list.remove(color)

print(colors_list)
