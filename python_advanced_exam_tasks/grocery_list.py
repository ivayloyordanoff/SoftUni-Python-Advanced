def shop_from_grocery_list(budget, grocery_list, *products):
    bought_products = []

    for product, price in products:
        if budget < price:
            break

        if product not in bought_products and product in grocery_list:
            budget -= price
            bought_products.append(product)
            grocery_list.remove(product)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = ', '.join(f"{product}" for product in grocery_list)
        return f"You did not buy all the products. Missing products: {result}."
