# Hozzatok létre egy sum fv-t ami paraméterül egész számok listáját kapja
# összegzi ezeket és az összeggel tér vissza

def sum_numbers(list_of_numbers):  # ne használjunk változó névben típus nevet
    result = 0
    for num in list_of_numbers:
        result += num
    return result


# Számolás tétele
# Írjatok egy olyan függvényt, ami paraméterül kap
# egy stringet és visszaadja, hogy hány magyar ékezetes
# karakter tartalmaz!

def count_accented(word):
    result = 0
    accent = ["á", "é", "í", "ü", "ű", "ú", "ö", "ő", "Á", "É", "Ö", "Ő", "Ü", "Ű", "Í"]

    for char in word:
        if (char in accent):
            result += 1
    return result


def count_accented_new(word):
    counter = 0

    for char in word:
        if ord(char) > 122:
            counter += 1
    return counter


# szélsőérték keresés
# írj egy függvényt ami visszaadja mai visszadja a leghosszabb szót
# a paraméterként átadott szövegből. A szövegben a szavakat space-ek 
# választják el egymástól


def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def find_longest_word(text):   # oktatói változat
    max_length = 0
    for word in text.split():
        actual_length = len(word)
        if actual_length > max_length:
            max_length = actual_length
            result = word  # üres stringnél hibát dob, mivel a result csak a for alatt van deklarálva
    return result


# Eldöntés tétele
# írj egy fv-t, amely eldönti egy listáról, hogy csak
# pozitív számokat tartalmaz-e! Ha egy 0 vagy negatív szám is
# van benn, akkor térjen vissza False értékkel!

def check_for_natural_numbers(numbers: list[int]) -> bool:
    for num in numbers:
        if num <= 0:
            return False
    return True


# Szűrés
# Írjatok egy olyan fv.-t ami paraméterül kap neveket listában
# és csak a J betűvel kezdődő neveket adja vissza
def find_names_with_J(names):
    result = []
    for name in names:
        if name[0].lower() == "j":
            result.append(name)

    return result


# szűrés list comprehension-nel
def find_names_of_J(names: list[str]) -> list[str]:
    result = [name for name in names if name.lower().startswith("j")]
    return result


# Transzformáció
# Írjatok egy olyan fv.-t amely paraméterül egy számok listáját kapja 
# és visszaad egy listát a számok abszolútértékével!
def get_absolute_values(numbers):
    absolute_values = []
    for num in numbers:
        if num <= 0:
            absolute_values.append(0-num)
        else:
            absolute_values.append(num)

    return absolute_values


# transzformáció list comprehensio-nel
def transform_to_absolute(numbers: list[int]) -> list[int]:
    absolutes = [abs(num) for num in numbers]
    return absolutes

# print("hello modul")
# print(f"a __name___ valtozo erteke: {__name__}")

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(sum_numbers(my_list))

    print(count_accented("bármicsakszöveglegyen"))

    print(count_accented_new("akármiÉkezetes"))

    print(longest_word("valami szöveg csak úgy"))

    print(find_names_with_J(["James", "John", "Tom", "Hedwig"]))

    print(get_absolute_values([3, 4, 5, -7, 0, -2]))

    print(find_names_of_J(["James", "John", "Tom", "Hedwig"]))

    print(transform_to_absolute([3, 4, 5, -7, 0, -2]))
