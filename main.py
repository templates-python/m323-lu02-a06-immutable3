"""Einkaufsliste.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/immutable3
"""

products = [
    {'product': 'Apple', 'quantity': 5, 'price': 1.2},
    {'product': 'Banana', 'quantity': 2, 'price': 0.8},
    # Add more products as needed
]

new_prices = {
    'Apple': 0.5,
    'Banana': 0.3,
    # Add more prices as needed
}


def update_prices(product_list, price_updates):
    updated_products = []
    for product in product_list:
        updated_product = product.copy()
        product_name = updated_product['product']
        if product_name in price_updates:
            updated_product['price'] = price_updates[product_name]
        updated_products.append(updated_product)
    return updated_products


def calculate_total(product_list):
    total = 0
    for product in product_list:
        total += product['price'] * product['quantity']
    return total


if __name__ == '__main__':
    demo_updated_products = update_prices(products, new_prices)
    print('Ursprüngliche Produkte:', products)
    print('Aktualisierte Produkte:', demo_updated_products)
    print('Gesamtpreis (alt):', calculate_total(products))
    print('Gesamtpreis (neu):', calculate_total(demo_updated_products))
