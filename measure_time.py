from datetime import datetime
import time


def time_decorator(function):
    def wrapper(*args):  # fv-ből függvénnyel kell visszatérni, a wrapper nem kötött
        start = datetime.now()
        result = function(*args)
        end = datetime.now()
        print(end-start)
        return result
    return wrapper

@time_decorator
def dummy(name):
    time.sleep(2)
    print(name)

dummy("JOhn Doe")  # figyeljünk ha paramétert akarunk átadni
