from sys import argv
name, time, money, bonus = argv
time = int(time)
money = int(money)
bonus = int(bonus)
z = (time * money) + bonus
print({z})
print(f'Заработная плата сотрудника составит: {z}')