def forecast(*args):
    weather_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for arg in args:
        weather_dict[arg[1]].append(arg[0])

    result = []

    for weather in ["Sunny", "Cloudy", "Rainy"]:
        locations = sorted(weather_dict[weather])

        for location in locations:
            result.append(f"{location} - {weather}")

    return "\n".join(result)
