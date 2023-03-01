def is_balanced(parentheses):
    stack = []
    for char in parentheses:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return "NO"
            elif char == ")" and stack[-1] != "(":
                return "NO"
            elif char == "]" and stack[-1] != "[":
                return "NO"
            elif char == "}" and stack[-1] != "{":
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"


print(is_balanced(input()))
