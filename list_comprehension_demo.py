fruits = ["apple", "banana", "cherry"]

upper_fruit = [fruit.upper() for fruit in fruits]  # for ciklussal végigmegyünk a fruits lista elemein,
# és azt nagybetűsítjük, amiből létre hozunk egy listát

print(upper_fruit)

numbers = [1, 3, 6, 2, 8, 7, 9]
filtered = [number for number in numbers if number % 2 == 0]
print(filtered)

filtered = [number**2 for number in numbers if number % 2 == 0]
print(filtered)
