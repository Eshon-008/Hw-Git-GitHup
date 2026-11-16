def count_vowels_and_consonants(text: str) -> dict:
    vowels = "aeiou"
    unli = 0
    undosh = 0

    for ch in text.lower():
        if not ch.isalpha():
            continue
        if ch in vowels:
            unli += 1
        else:
            undosh += 1

    return {"unli": unli, "undosh": undosh}


print(count_vowels_and_consonants("Salom Dunyo!"))
print(count_vowels_and_consonants("Python 3!"))
print(count_vowels_and_consonants("Hello, World!"))




# -------------------      2 - masala              --------------------------------
def find_top_seller(products: dict, sales: dict) -> str:
    revenue = {name: price * sales[name] for name, price in products.items()}
    return max(revenue, key=revenue.get)


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))