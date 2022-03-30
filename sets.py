# Halmazok

numbers = {2, 3, 6, 8}

numbers.add(9)
print(numbers)

# nem fog a 2-es kétszer szerepelni benne
numbers.add(2)
print(numbers)

print(len(numbers))  # van hossza


for i in numbers:  # be lehet járni
    print(i)

numbers.remove(3)
print(numbers)

words = ["xxx", "yyy", "zzz", "xxx"]
print(words)
words_set = set(words)  # bármi ami iterálható, abból lehet halmazt készíteni a set()-tel
print(words_set)

print("xxx" in words_set)

letters1 = {"a", "b", "c", "e", "f", "g"}
letters2 =set("efgxyz")  # karakterekre bontja a stringet

print(f"letters1: {letters1}")
print(f"letters2: {letters2}")

print(letters1.union(letters2))
print(letters1 | letters2)  # logikai vagy = unio
print(letters1.intersection(letters2))
print(letters1 & letters2)  # logikai és = metszet

print(letters1.difference(letters2))
print(letters1 - letters2)

print(set("bc").issubset(letters1))
print(set("bc") < letters1)

# hány különböző betű van egy szóban
print(len(set("aaabbbcccd")))

# módosíthatatlan halmaz ==>
colors = frozenset({"green", "black", "yellow"})
print(colors)
