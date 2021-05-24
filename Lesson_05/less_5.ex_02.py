with open('2.txt', 'r+') as f:
    m_line = f.readlines()
    i = 0
    for x in m_line:
        print(f'В строке {i+1} {len(x.split())} слов')
        i += 1
    print(f'Количество срок {len(m_line)}')
