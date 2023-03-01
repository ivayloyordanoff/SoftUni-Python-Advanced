from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
pieces_of_paper = deque([int(x) for x in input().split(", ")])

box_size = 50
boxes_filled = 0

while eggs and pieces_of_paper:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    elif egg == 13:
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue
    else:
        piece_of_paper = pieces_of_paper.pop()
        wrapped_egg = egg + piece_of_paper

        if wrapped_egg <= box_size:
            boxes_filled += 1

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in pieces_of_paper)}")
