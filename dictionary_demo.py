employee = {"name": "John Doe", "year_of_birth": 1980}
print(employee["name"])
print(employee["year_of_birth"])

employee["favourite_color"] = "red"
print(employee)
employee["favourite_color"] = "blue"
print(employee)

del employee["favourite_color"]
print(employee)

inventory = {"banana": 1, "melon": 2, "apple": 3}
print(inventory["banana"])

print(len(inventory))  # hány bejegyzése van

# for ciklus a kulcsokon megy végig, elég lassú
for i in inventory:
    print(i)
    print(inventory[i])

# type2 - gyorsabb, mivel kulcs értékpárt fog meg egyszerre, a
# a.items()  <-- egy kulcs: iterátor pár tuple-t ad vissza
for (k, v) in inventory.items():
    print(f"A '{k}' termékből {v} darab található a raktárban")


# hisztogram készítése
def count_numbers(numbers):
    counts = {}
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return counts

print(count_numbers([1, 1, 1, 2, 3, 4, 3, 4, 2])) 

result = count_numbers([1, 1, 1, 1, 2, 2])
print(result == {1: 4, 2: 2})
print(result == {2: 2, 1: 1})

print(result.keys())
print(result.values())

# szótárban egy lista aminek értékei tuple
employee = {"name": "John Doe", "year_of_birth": 1990, "skills": [("java", 3), ("python", 5)]}
print(employee["skills"][1][1])

# írjatok egy fv-t, amely megszámolja, hogy a kapott stringben
# melyik betű hányszor szerepel
# B) csak betűket számoljon, és ábécé sorrendben írja ki egymás alá

def is_abc(char):  # .isalpha()
    if char.lower() in "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz":
        return True
    else:
        return False

def count_characters(text):
    numbers_of_characters = {}
    for c in text:
        c = c.lower()
        if is_abc(c):
            if c not in numbers_of_characters:
                numbers_of_characters[c] = 1
            else:
                numbers_of_characters[c] +=1
    return numbers_of_characters

result = count_characters("valami#szöveg3")
print(result)

# a kulcsokat kipakoljuk egy listába
# a listát tudjuk rendezni, majd a listán végigmenve, azokhoz a kulcsokhoz hozzáhívjuk a számokat
letters = list(result.keys())
letters.sort()
for letter in letters:
    print(f"{letter}: {result[letter]}")

# tuple unpack
values = ("John Doe", 1985)
name, year_of_birth = values
print(name)
print(year_of_birth)


# buil-in function: enumerate()
numbers = [7, 8, 7, 8, 7, 8]
for i in range(0, len(numbers)):
    print(f"{i}: {numbers[i]}")

i=0
for n in numbers:
    i += 1
    print(f"{i}: {n}")

print(list(enumerate(numbers, start=1)))  # visszaad egy tuple listát (index, érték)

for i,n in enumerate(numbers, start=1):
    print(f"{i}: {n}")

# dictionary comprehension
doubles = {i: i**2 for i in range(10)}
print(doubles)