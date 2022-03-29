names = ["Jane", "Jack", "John"]

employees = names  # az employees megkapja a names-ben tárolt 32 bites memória cím
print(employees)

names[1] = "Jack XY"
print(employees)  # szintén Jack XY fog szerepelni benne

employees[2] = "John XY"  # módosítja a names-t is

# olyan mintha 2 névvel hivatkoznánk ugyan arr a amemória címre

# másolatot készíteni:
# workers = names.copy()
workers = names[:]  # szeletelés mindig új listát ad vissza
names[0] = "JaneXYZ"

# objektum azonosítók
print(id(names))
print(id(employees))
print(id(workers))
