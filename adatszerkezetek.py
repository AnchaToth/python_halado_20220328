["Jack", "John"]  # memóriába beírjuk, viszont nem hivatkozik rá semmi
names = ["Jack", "John"]  # névvel hiavtkozunk a memória területre

print(names == ["Jack", "John"])

names.append("Jane")  # a memória objektumon hívja meg a függvényt, és változtatja az ott tárolt értéket azaz az objektum állapotát

names[1] = "John XY"


fruit = "cherry"
upper_name = fruit.upper()
print(fruit.upper())
