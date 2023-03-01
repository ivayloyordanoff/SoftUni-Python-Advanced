from collections import deque

caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

max_caffeine = 300
total_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    sum_of_caffeine = current_caffeine * current_energy_drink

    if sum_of_caffeine <= max_caffeine:
        total_caffeine += sum_of_caffeine
        max_caffeine -= sum_of_caffeine
    else:
        energy_drinks.append(current_energy_drink)
        total_caffeine -= 30
        max_caffeine += 30

        if total_caffeine < 0:
            total_caffeine = 0

        if max_caffeine > 300:
            max_caffeine = 300

if energy_drinks:
    print(f"Drinks left: {', '.join(str(drink) for drink in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
