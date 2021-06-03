class Office:

    def __init__(self, name, price, quan):
        self.name = name
        self.price = price
        self.quant = quan
        self.my_list = {'Устройство': self.name, 'Цена за 1 ед.': self.price, 'Количество': self.quant}

    def obj(self):
        try:
            name = input('Введите наименование: ')
            priсe = int(input('Введите цену за 1 ед.: '))
            quan = int(input('Введите количтво: '))
            my_list = {'Устройство': name, 'Цена за 1 ед.':priсe, 'Количество': quan}
            self.my_list.items(my_list)
            print(self.my_list)
        except:
            print('Значените введно не верно')


class Printer(Office):
    pass


class Scanner(Office):
    pass


class Xerox(Office):
    pass


p = Printer('Hp', 6000, 5)
s = Scanner('Canon', 5500,10)
x = Xerox('Xerox', 8000, 22)
p.obj()
s.obj()
x.obj()

