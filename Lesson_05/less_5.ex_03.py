from statistics import mean

with open('3.txt', 'r+') as m_file:
    m_list = []
    man = []
    money = []
    content = m_file.read()
    m_list = content.split('\n')
    for i in m_list:
        i = i.split()
        if int(i[1]) > 20000:
            man.append(i[0])
        money.append(int(i[1]))
m_mean = mean(money)
# print(m_list)
# print(man)
# print(money)
# print(m_mean)
print(f'Сотрудники имеющие окдад менне 20 000 {man}, средний доход сотрудников составил {m_mean}')