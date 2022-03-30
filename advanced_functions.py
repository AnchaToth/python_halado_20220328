from datetime import datetime
import time

def sum(*args):  #csillaggal jelezzük, hogy akárhány paraméter átadható
    print(args)
    print(type(args))

sum(1, 2, 3, 4)

def add(a, b):
    return a+b

print(add(1, 2))

number_pair = (3, 4)
print(add(*number_pair))  # a tuple 1. értéke lesz az 1. a második pedig a 2. paraméter
# = print(add(number_pair[0], number_pair[1]))

def print_employee(**kwargs):
    print(type(kwargs))
    print(kwargs)
 

print_employee(name="John Doe", age=40)

number_pair = {"a": 1, "b": 2}
print(add(**number_pair))

print("aaa", "bbb", "ccc", sep="***")

# 
def substract(a, b):
    return a - b

print(substract(6, 2))

kivon = substract  # fv-t értékül adhatjuk a változónak, onnantól kezdve a változó arra  fv-re mutat
print(kivon(6, 2))

# lambda kifejezések, névtelen fv-ek?

reverse = lambda s: s[::-1]  # ezt sehol máshol nem fogjuk tudni használni
# jobb oldal: hozz létre egy fv-t egy s paraméterrel
# térjen vissza a paraméter fordított
print(reverse("körte"))

def print_name():
    print("oktató")

def haromszor(ezt_csinald):
    for i in range(3):
        ezt_csinald()

haromszor(print_name)

# lambdaval
haromszor(lambda :print("hello"))


# számoljátok meg egy hosszú szövegben, hogy melyik szó
# hányszor szerepel


# dekorátor függvény
def uppercase_decorator(function):
    def wrapper():  # dekorátor
        value = function()
        return value.upper()
    return wrapper

@uppercase_decorator
def say_my_name():
    return "John Doe"

print(say_my_name())


# pl. logolás

def log_decorator(function):
    def wrapper():
        now = datetime.now()
        print(str(now) + " " + function.__name__ + " " + function.__doc__)
        return function()
    return wrapper

@log_decorator
def transfer():
    """Transfer between accounts"""
    x = 1 + 2
    print("lefut?")

@log_decorator
def create_client():
    """Create client"""
    name = "John Doe"

transfer()
create_client()

start = datetime.now()
time.sleep(3)
stop = datetime.now()

diff = stop-start
print(diff)