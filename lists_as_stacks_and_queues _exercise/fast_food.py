from collections import deque

food_quantity = int(input())
orders = list(map(int, input().split(' ')))
queue = deque(orders)

print(max(queue))

for order in queue.copy():
    if food_quantity - order >= 0:
        food_quantity -= order
        queue.popleft()
    else:
        break

if not queue:
    print("Orders complete")
else:
    print("Orders left: ", end="")
    while queue:
        print(queue.popleft(), end=" ")
