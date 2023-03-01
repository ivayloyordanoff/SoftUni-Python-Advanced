def shopping_cart(*args):
    meals = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    for arg in args:
        if arg == "Stop":
            break

        meal, product = arg[0], arg[1]

        if meal == "Soup" and len(meals[meal]) < 3 and product not in meals[meal]:
            meals[meal].append(product)
        elif meal == "Pizza" and len(meals[meal]) < 4 and product not in meals[meal]:
            meals[meal].append(product)
        elif meal == "Dessert" and len(meals[meal]) < 2 and product not in meals[meal]:
            meals[meal].append(product)

    for product in meals.values():
        if len(product) > 0:
            break
    else:
        return f"No products in the cart!"

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for meal in sorted_meals:
        result += f"{meal[0]}:\n"
        sorted_products = sorted(meal[1])

        for product in sorted_products:
            result += f" - {product}\n"

    return result
