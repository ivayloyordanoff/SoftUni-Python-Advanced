from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

patch = 30
bandage = 40
medkit = 100

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    current_sum = textile + medicament

    if current_sum == patch:
        created_items["Patch"] += 1
    elif current_sum == bandage:
        created_items["Bandage"] += 1
    elif current_sum == medkit:
        created_items["MedKit"] += 1
    elif current_sum > medkit:
        created_items["MedKit"] += 1
        remaining_resources = current_sum - medkit
        medicaments[-1] += remaining_resources
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x))

for key, value in sorted_items:
    if not value == 0:
        print(f"{key} - {value}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
