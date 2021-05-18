num = input('Введите число:')
list = [7, 5, 3, 3, 2]
a = int(num)
if a == 1:
    list.append(1)
# print(list)
if not a == 1:
       for i in list:
        x = int(i)
        if x <= a:
            w = int(list.index(i))
            list.insert(w, a)
            break
print(list)
