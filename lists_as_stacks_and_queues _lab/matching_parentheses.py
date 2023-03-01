data = input()
parentheses = []

for i in range(len(data)):
    if data[i] == "(":
        parentheses.append(i)
    elif data[i] == ")":
        start_index = parentheses.pop()
        print(data[start_index: i + 1])
