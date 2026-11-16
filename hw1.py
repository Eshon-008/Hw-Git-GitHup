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