number = int(input())
stack = []

for _ in range(number):
    command = input().split(" ")
    if command[0] == "1":
        current_number = int(command[1])
        stack.append(current_number)
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        if stack:
            print(max(stack))
    elif command[0] == "4":
        if stack:
            print(min(stack))

print(*stack[::-1], sep=", ")
