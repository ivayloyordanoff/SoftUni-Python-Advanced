from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()

    if current_magic_level == 0 and current_material == 0:
        continue
    elif current_magic_level == 0:
        materials.append(current_material)
        continue
    elif current_material == 0:
        magic_levels.appendleft(current_magic_level)
        continue

    product = current_material * current_magic_level

    if product in presents:
        crafted.append(presents[product])
    elif product < 0:
        materials.append(current_material + current_magic_level)
    elif product > 0:
        materials.append(current_material + 15)

if presents[150] in crafted and presents[250] in crafted or presents[300] in crafted and presents[400] in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present in sorted(set(crafted)):
    print(f"{present}: {crafted.count(present)}")
