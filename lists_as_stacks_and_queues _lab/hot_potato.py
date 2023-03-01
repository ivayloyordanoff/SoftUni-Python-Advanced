from collections import deque

names_of_kids = input().split(" ")
toss = int(input())
queue = deque(names_of_kids)

while len(queue) > 1:
    for _ in range(toss - 1):
        queue.append(queue.popleft())

    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.popleft()}")
