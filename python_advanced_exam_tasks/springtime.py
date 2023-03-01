def start_spring(**kwargs):
    data = {}

    for key, value in kwargs.items():
        if value in data:
            data[value].append(key)
        else:
            data[value] = [key]

    sorted_data = sorted(data.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for current_data in sorted_data:
        result += f"{current_data[0]}:\n"
        sorted_objects = sorted(current_data[1])

        for current_object in sorted_objects:
            result += f"-{current_object}\n"

    return result
