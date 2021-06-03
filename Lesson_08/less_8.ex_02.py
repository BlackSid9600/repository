class Erorr:
    def __init__(self, num):
        self.num = num


def div():
    try:
        num_1 = int(input('Введите число (делимое):'))
        num_2 = int(input('Введите число (делеитель):'))
        if num_2 == 0:
            print('На ноль делть нельзя!')
        else:
            return f'{num_1 / num_2}'
    except ValueError:
        return 'Вы ввели не число!'


print(div())

