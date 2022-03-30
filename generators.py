def firstn(n):
    result = []
    i = 0
    while i < n:
        result.append(i)
        i += 1
    return result

print(sum(firstn(100)))


# más módon, generátor függvénnyel
def firstn2(n):
    i = 0
    while i < n:
        yield i  # nem állít elő egy listát előre, csak mindig a következő elemet a megadott szabály alapján
        i+= 1

print(sum(firstn2(100)))

for n in firstn2(20):
    print(n)

