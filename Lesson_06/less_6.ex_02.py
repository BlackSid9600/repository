km = input('Введите длинну дороги в метрах:')
cm = input('Введите ширину дороги в метрах:')

class Road:


    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width
        # print(self.length)

    def coat(self):
        t = (int(self.__length) * int(self.__width) * 25 * 5) / 1000
        print(f'Для покрытия данного участка дороги понадобится {t} тонн асфальта')

r = Road(km, cm)
r.coat()


