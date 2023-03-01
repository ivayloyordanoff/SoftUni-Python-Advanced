codes = {input() for _ in range(int(input()))}
counter = len(codes)
COMMAND_END = "END"

while True:
    command = input()

    if command == COMMAND_END:
        break

    if command in codes:
        codes.remove(command)
        counter -= 1

print(counter)

for code in sorted(codes):
    print(code)
