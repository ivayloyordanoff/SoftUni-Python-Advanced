box_clothes = list(map(int, input().split()))
rack_capacity = int(input())
total_racks = 1
current_rack_capacity = rack_capacity

while box_clothes:
    cloth = box_clothes.pop()

    if current_rack_capacity - cloth >= 0:
        current_rack_capacity -= cloth

    else:
        total_racks += 1
        current_rack_capacity = rack_capacity - cloth

print(total_racks)
