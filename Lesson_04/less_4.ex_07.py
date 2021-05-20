import math
from itertools import count
from math import factorial
from functools import reduce
x = int(input('Введитетчисло:'))

# for el in fact(n):

new_list = [el for el in range(1, x + 1)]
def my_func(el1, el2):
    return el1 * el2
print(f'Результат вычисления {reduce(my_func, (new_list))}')


print(f'Факториал {factorial(x)}')
