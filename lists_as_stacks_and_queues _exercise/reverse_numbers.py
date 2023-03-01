from collections import deque

queue = deque(input().split())
queue.reverse()

print(" ".join(queue))
