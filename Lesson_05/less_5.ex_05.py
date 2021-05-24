with open('5.txt', 'r+') as m_file:
    content = m_file.read()
    # print(f'{content}')
    x = 0
    s_list = content.split()
    for nom in s_list:
        x += int(nom)
print(f'Сумма чисел в файле {x}')