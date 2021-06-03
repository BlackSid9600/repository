class Data:


    def __init__(self, x_date):
        self.x_date = str(x_date)

    @classmethod
    def day_date(cls, x_date):
        my_dete = []

        for i in x_date.split(' '):
            if i != '-': my_dete.append(i)

        # return f'{my_dete[0], my_dete[0], my_dete[0]}'
        return int(my_dete[0]), int(my_dete[1]), int(my_dete[2])


    @staticmethod
    def check(DD, MM, YYYY):
        if 1 <= DD <= 31:
            if 1 <= MM <= 12:
                if 1700 <= YYYY:
                    return f'Все правильно!'
                else:
                    return f'Неверно введен год!'
            else:
                return f'Неверно введен месяц!'
        else:
            return f'Неверно введен день!'

    def __str__(self):
        return f'Дата {Data.day_date(self.x_date)}'


date = Data('13 - 09 - 2005')
print(date)

print(date.check(13, 9, 2005))
print(date.check(33, 9, 2005))
print(date.check(3, 13, 2005))
print(date.check(3, 12, 1699))

print(Data.day_date('12 - 12 - 2005'))
