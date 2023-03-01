from custom_modules.fibonacci_sequence import create_fibonacci_sequence, locate_number


def fibonacci_sequence():
    while True:
        command = input()

        if command.startswith("Stop"):
            break
        elif command.startswith("Create"):
            print(create_fibonacci_sequence(int(command.split()[2])))
        elif command.startswith("Locate"):
            print(locate_number(int(command.split()[1])))


fibonacci_sequence()
