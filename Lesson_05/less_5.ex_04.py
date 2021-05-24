with open('4.txt', 'r+') as m_file:
    x = []
    for line in m_file:
        nom = line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
        # f = open('4.1.txt', 'w')
        # print(nom)
        # x.append()
        x.append(nom)
# print(x)
with open('4.1.txt', 'w+', encoding='utf-8') as o_file:
     o_file.writelines(x)
print(f'Файл 4.1.txt создан.')