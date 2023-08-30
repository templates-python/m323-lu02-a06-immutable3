products = [
    {'product': 'Apple', 'quantity': 5, 'price': 1.2},
    {'product': 'Banana', 'quantity': 2, 'price': 0.8},
    # Add more products as needed
]

prices = {
    'Apple': 0.5,
    'Banana': 0.3,
    # Add more prices as needed
}


def update_prices(products, new_prices):
    updated_products = []
    for product in products:
        updated_product = product.copy()
        product_name = updated_product['product']
        if product_name in new_prices:
            updated_product['price'] = new_prices[product_name]
        updated_products.append(updated_product)
    return updated_products


def calculate_total(products):
    total = 0
    for product in products:
        total += product['price'] * product['quantity']
    return total


if __name__ == '__main__':
    updated_products = update_prices(products, prices)
    print("Ursprüngliche Produkte:", products)
    print("Aktualisierte Produkte:", updated_products)
    print("Gesamtpreis (alt):", calculate_total(products))
    print("Gesamtpreis (neu):", calculate_total(updated_products))
