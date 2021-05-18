words = input('Введите слова через пробел:')
for num, el in enumerate(words.split(' ')):
    print(num + 1, el[0:10])