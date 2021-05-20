set_list = [20, 240]
new_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0 ]
print(f'Вводные данные {set_list}')
print(f'Результат {new_list}')
