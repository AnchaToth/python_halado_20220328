# egy konkrét függvényt importálunk a modulból
#from prg_tetelek import sum_numbers
#print(sum_numbers([1,2,3,4,5]))

# az egész modul importáljuk
#import prg_tetelek
#print(prg_tetelek.sum_numbers([1,2,3]))

# Minden függvényt a modulból
#from prg_tetelek import *
#print(sum_numbers([2,4,6]))

 ## alias-sal importáljuk az egész modult.
import prg_tetelek as algs
print(algs.sum_numbers([3,6,9]))