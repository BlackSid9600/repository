from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

x = 0
for el1 in cycle('SiD'):
    if x > 10:
        break
    print(el1)
    x += 1
