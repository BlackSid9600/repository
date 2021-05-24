input_sec = int(input('Введите время в секундах:'))
hours = input_sec // 3600
min = (input_sec - (hours * 3600)) // 60
sec = input_sec % 60
print(hours, ':', min,':',sec)