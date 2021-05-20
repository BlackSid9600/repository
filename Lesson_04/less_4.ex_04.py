list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list if list.count(el) == 1]
print(f'Вводные данные {list}')
print(f'Результат {new_list}')