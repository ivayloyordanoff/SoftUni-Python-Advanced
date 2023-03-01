def words_sorting(*words):
    data = {}
    values_sum = 0

    for word in words:
        data[word] = 0

        for letter in word:
            data[word] += (ord(letter))

    for value in data.values():
        values_sum += value

    if values_sum % 2 == 0:
        sorted_data = sorted(data.items(), key=lambda x: x[0])
    else:
        sorted_data = sorted(data.items(), key=lambda x: -x[1])

    result = ""

    for key, value in sorted_data:
        result += f"{key} - {value}\n"

    return result
