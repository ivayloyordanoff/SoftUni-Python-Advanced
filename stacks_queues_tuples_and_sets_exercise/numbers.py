first_set = {int(num) for num in input().split()}
second_set = {int(num) for num in input().split()}

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if command == "Add First":
        [first_set.add(int(num)) for num in data]
    elif command == "Add Second":
        [second_set.add(int(num)) for num in data]
    elif command == "Remove First":
        [first_set.discard(int(num)) for num in data]
    elif command == "Remove Second":
        [second_set.discard(int(num)) for num in data]
    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
