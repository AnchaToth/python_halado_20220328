print("furó" in "árvíztűrőtükörfúrógép")
print(5 in [1, 2, 3, 4, 5])

print("árvíztűrőtükörfúrógép".index("fúró"))
print("árvíztűrőtükörfúrógép".find("fúró"))

# print("árvíztűrőtükörfúrógép".index("XY"))  # Value Error ha nincs benne
print("árvíztűrőtükörfúrógép".find("XY"))

print([1, 2, 3].index(2))
# print([1,2,3].index(6))  # Value error

print("xyxyxyxyxxx".count("x"))

# következő előfordulást keresi, azaz az adott index utánit
print("almaalmaalma".find("a", 2))

# Írj egy olyan fv-t, ami egy stringben megkeresi egy substring összes
# előfordulását és visszaadja a pozíciókat egy listában
# "almaalmaalma", "alma" --> [0, 4, 9]
# egszer, kétszer, átlapolva, nincs benne, a keresett szó hosszabb


def find_substring(text: str, substring: str):
    i = 0
    positions = []
    if text.find(substring) != -1:
        while i < len(text):
            positions.append(text.find(substring, i))
            i = i + len(substring)

    return positions


print(find_substring("almaalmalma", "alma"))

# oktatói;


def find_all_occurences(text, sub):
    result = []
    i = 0
    while i < len(text) - len(sub) + 1:
        if text[i: i + len(sub)] == sub:
            result.append(i)
            i += len(sub)
        else:
            i += 1
    return result


# Rendezés

numbers = [32, 64, 128, 256, 14, 12, 8]
print(sorted(numbers))  # új, rendezett listát ad vissza
print(numbers)
print("****")
numbers.sort()  # az adott listát rendezi
print(numbers)
