def my_sum():
    sum = 0
    ex = False
    while ex == False:
        number = input('Введиете число, либо "Q" для выхода:').split()
        x = 0
        for el in range(len(number)):
             if number[el] == 'Q' or number[el] == 'q':
                 ex == True
                 break
             else:
                 x = x + int(number[el])
        sum = sum + x
        print(f'Сумма {sum}')
my_sum()
