#Hozzatok létre egy sum fv-t ami paraméterül egész számok listáját kapja
#összegzi ezeket és az összeggel tér vissza

def sum_numbers(list_of_numbers):  ##  ne használjunk változó névben típus nevet
    result = 0
    for num in list_of_numbers:
        result += num
    return result


## Számolás tétele
# Írjatok egy olyan függvényt, ami paraméterül kap
# egy stringet és visszaadja, hogy hány magyar ékezetes
# karakter tartalmaz!

def count_accented(word):
    result = 0
    accent = ["á","é","í","ü","ű","ú","ö","ő","Á","É","Ö","Ő","Ü","Ű","Í"]

    for char in word:
        if (char in accent):
            result +=1
    
    return result

def count_accented_new(word):
    counter = 0

    for char in word:
        if ord(char) > 122:
            counter += 1
    return counter

## szélsőérték keresés
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

def find_longest_word(text):   ##  oktatói változat
    max_length = 0
    for word in text.split():
        actual_length = len(word)
        if actual_length > max_length:
            max_length = actual_length
            result = word       ##  üres stringnél hibát dob, mivel a result csak a for alatt van deklarálva
    return result


## Eldöntés tétele
# írj egy fv-t, amely eldönti egy listáról, hogy csak
# pozitív számokat tartalmaz-e! Ha egy 0 vagy negatív szám is
# van benn, akkor térjen vissza False értékkel!

def check_for_natural_numbers(numbers: list[int]) -> bool:
    for num in numbers:
        if num <= 0:
            return False
    return True


#print("hello modul")
#print(f"a __name___ valtozo erteke: {__name__}")

if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9]

    print(sum_numbers(my_list))

    print(count_accented("bármicsakszöveglegyen"))

    print(count_accented_new("akármiÉkezetes"))

    print(longest_word("valami szöveg csak úgy"))
