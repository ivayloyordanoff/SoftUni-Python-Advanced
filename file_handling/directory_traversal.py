import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        current_file = os.path.join(dir_name, filename)

        if os.path.isfile(current_file):
            current_extension = filename.split(".")[-1]

            if current_extension not in extensions:
                extensions[current_extension] = []

            extensions[current_extension].append(filename)

        elif os.path.isdir(current_file) and not first_level:
            save_extensions(current_file, first_level=True)


directory = input()
extensions = {}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - -{file}")

with open(f"files/report.txt", "w") as file:
    file.write("\n".join(result))
