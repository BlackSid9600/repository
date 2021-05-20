from functools import reduce
new_list = [el  for el in range(100, 1001, 2)]
def my_func(el1, el2):
    return el1 + el2
print(f'Список {new_list}')
print(f'Результат вычисления произведения всех элементов списка равен {reduce(my_func, (new_list))}')
