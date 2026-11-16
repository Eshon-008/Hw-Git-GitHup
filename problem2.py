def find_top_seller(products: dict, sales: dict) -> str:
    revenue = {name: price * sales[name] for name, price in products.items()}
    return max(revenue, key=revenue.get)


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))