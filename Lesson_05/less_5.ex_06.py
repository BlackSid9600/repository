with open('6.txt', 'r+', encoding = 'utf-8') as my_file:
    d = {}
    list = []
    for my_line in my_file:
#        name, lec, prac, lab = my_line.split()
#        sub[name] = int(lec) + int(prac) + int(lab)
# print(sub)
        key = my_line.split(' ')[0]
        value = my_line.split(' ')[1:4]


        d[key] = value
        print(value)
    # print(val[0])
    # print(value, val)
    # print(x)
