def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese_name, quantity in sorted_data:
        result.append(cheese_name)
        result.extend(sorted(quantity, reverse=True))

    return "\n".join(str(x) for x in result)
