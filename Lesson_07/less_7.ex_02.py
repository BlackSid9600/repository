class Size():


    def __init__(self, v, h):
        self.v = v
        self.h = h

    def sum_coat(self):
        # return format(((self.v / 6.5) + 0.5), '.2f')
        return (self.v / 6.5) + 0.5

    def sum_suit(self):
        # return format(((self.h * 2) + 0.3), '.2f')
        return ((self.h * 2) + 0.3)

    def __add__(self, other):
        return Size((self.v / 6.5) + 0.5, (self.h * 2) + 0.3)

    def __str__(self):
        return f"Всего понадобится ткани: {format(self.v + self.h, '.0f')}"

    def sum_all(self):
        x =  format((self.sum_coat() + self.sum_suit()), '.2f')
        return f'Всего {x} ткани понадобится'



class Coat(Size):


    def __init__(self, v, h):
        Size.__init__(self, v, h)

    def fabric_coat(self):
        # fc = format((self.v / 6.5) + 0.5, '.2f')
        fc = format((round(self.sum_coat())), '.2f')
        print(f'{fc} ткани понадобится для пошива 1 пальто.')
        # return f'{fc} ткани понадобится для пошива 1 пальто.'


class Suit(Size):


    def __init__(self, v, h):
        Size.__init__(self, v, h)

    def fabric_suit(self):
       fs = format((round(self.sum_suit())), '.2f')
       print(f'{fs} ткани понадобится для пошива 1 костюма.')


class All_sum(Size):


    def __init__(self, v, h):
        Size.__init__(self, v, h)



coat = Coat(56, 180)
suit = Suit(56, 180)

coat.fabric_coat()
suit.fabric_suit()
print(coat + suit)
