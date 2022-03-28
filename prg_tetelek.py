#Hozzatok létre egy sum fv-t ami paraméterül egész számok listáját kapja
#összegzi ezeket és az összeggel tér vissza

def sum_numbers(list_of_numbers):  ##  ne használjunk változó névben típus nevet
    result = 0
    for num in list_of_numbers:
        result += num
    return result

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
        if ord(chr) > 122:
            counter += 1
    return counter

#print("hello modul")
#print(f"a __name___ valtozo erteke: {__name__}")

if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9]

    print(sum_numbers(my_list))

    print(count_accented("bármicsakszöveglegyen"))

    print(count_accented_new("akármiÉkezetes"))