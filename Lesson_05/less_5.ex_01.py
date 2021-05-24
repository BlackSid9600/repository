with open('1.txt', 'w') as x:

    content = input('Введите данные:')
    x.write(content)
    while content != ' ':
        content = input('Введите данные:')
        x.write(content)
print(content)
