from random import randint, random, randrange, choices, shuffle, Random
from secrets import choice

print(randint(0, 10))  # [0, 10]
print(random())  # [0, 1.0[  számokat adhat vissza
print(randrange(0, 10))  # [0, 10 [

names = ["Jack", "Jane", "Joe"]

print(choice(names))  # a parameterül kapott listából random visszaad egy elemet
print(choices(names, k=2))

shuffle(names)  # aktuális listát változtatja
print(names)

# írjunk egy fv-t az ötöslottó húzásra

def lotto():
    results = []
    i =0
    while i < 5:
        pick = randint(1, 90)
        if pick not in results:
            results.append(pick)
            i += 1
    return results

print(lotto())


def lotto_new():
    result = choices(range(1, 91), k=5)
    return result

print(lotto_new())

def generate_lotto_numbers(random=Random()):
    numbers = list(range(1, 91))
    random.shuffle(numbers)

    return(numbers[:5])

print(generate_lotto_numbers())
print(generate_lotto_numbers(Random(5)))
