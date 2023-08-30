import main

def test_update_price():
    """Test if the function correctly updates the prices."""
    new_prices = {'Apple': 1.5, 'Banana': 0.9}
    updated_list = main.update_price(main.products, new_prices)
    for item in updated_list:
        assert item['price'] == new_prices.get(item['product'], item['price']), \
            f"Expected {new_prices.get(item['product'], item['price'])}, but got {item['price']}."

def test_original_list_unchanged():
    """Test if the original product list remains unchanged."""
    original_list = main.products.copy()
    main.update_price(main.products, main.prices)
    assert main.products == original_list, f"Expected the original list to remain unchanged, but got {products}."

def test_calculate_total():
    """Test if the total cost is correctly calculated."""
    new_prices = {'Apple': 1.5, 'Banana': 0.9}
    updated_list = main.update_price(main.products, new_prices)
    total_cost = main.calculate_total(updated_list)
    expected_cost = sum(item['quantity'] * new_prices.get(item['product'], item['price']) for item in updated_list)
    assert total_cost == expected_cost, f"Expected {expected_cost}, but got {total_cost}."
