from functools import reduce

expression = input().split()

index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:index]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:index]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:index]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:index]),
}

while index < len(expression):
    element = expression[index]

    if element in "*/+-":
        result = functions[element](index)
        [expression.pop(0) for i in range(index)]
        expression[0] = result
        index = 0

    index += 1

print(int(expression[0]))
