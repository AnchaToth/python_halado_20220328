# írj egy függvényt, ami paraméterül kap egy listát és visszaad egy
# új listát, az eredeti lista minden második elemével
def pick_every_other(values):
# return values[::2]  # szeletelés
    even = False
    result = []
    for value in values:
        if even:
            result.append(value)
        even = not even
    
    return result

# Írj egy oylan fv.-t, ami kicseréli egy stringben az ékezetes karaktert
# a neki megfelelő nem ékezetes párjára
def replace_accented(text):
    accents ="áéíöőüűóú"
 
 # oktató
def replace_spec_chars(text):
    chars = "áéíöőüűóúÁÉÍÖÜÓŐÚŰ"
    pairs = "aeioouuouAEIOUOOUU"
    result = ""

    for c in text:
        if c in chars:
             result += pairs[chars.index(c)]
        else:
            result += c
    return result



# Írj egy oylan fv.-t, ami bekér a felhasználótól egész számokat amíg 0-t nem kap
# majd adja vissza ezeket egy listában
# ex.2 ha a felhasználó nem számot ad, dobjon hibát és fusson tovább a program

def write_your_choices():
    print("Give a natural number, you can terminate your list with 0: ")
    number = -1
    numbers =[]
    while number != 0:
        value = input()
        #try:
        #    number = int(value)
        #except ValueError:
        #    print(f"Wrong value: {value}")
        if value.isnumeric():
            number = int(value)
            if number != 0:
                numbers.append(number)
        else:
            print("The given value is not a number!")


    return numbers
    #print(numbers)

if __name__ == "__main__":
    write_your_choices()

    #print(replace_spec_chars("ékezetesszövegbármi"))
