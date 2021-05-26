km_in = float(input('Начальнй результат:'))
km_out = float(input('Конечнй результат:'))
day = 1
print(day, '- й день:', km_in)
while km_in < km_out:
    day = day + 1
    km_in = km_in + (km_in * 0.1)
    print(day, '- й день:', round(km_in, 2))

