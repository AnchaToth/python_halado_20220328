def a():
    x = "x"
    try:
        int(x)
    except ValueError as e:
        print(f"hiba {e}")
    except:
        print("nem tudom")


def b():
    y = "y"
    a()


def c():
    z = "z"
    b()

print("start")
c()
print("End")

try:
    print(55 / 0)  # ZeroDivisionError
except ZeroDivisionError:
    print("Nullával nem osztunk")

numbers =[1, 2, 3]
try:
    print(numbers[3])
except IndexError:
    print("rosszul indexelsz!")

try:
    "almakorte".index("x")
except ValueError:
    print("substring is not found in the word")
