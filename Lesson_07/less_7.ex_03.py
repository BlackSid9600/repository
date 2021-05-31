class Cell:


    def __init__(self, lot):
        self.lot = int(lot)
        # print(lot)

    # def __str__(self):
    #     return f'Результат опрерации {self.lot}'

    def __add__(self, other):
        return f'Результат сложения {self.lot + other.lot}'

    def __sub__(self, other):
        sub = self.lot - other.lot
        return f'Результат операции {sub}' if sub > 0 else 'Результат меньше 0'

    def __mul__(self, other):
        return f'Результат умножения {self.lot * other.lot}'

    def __truediv__(self, other):
        return f'Результат деления {self.lot // other.lot}'

    def make_order(self, in_row):
        row = ''
        for i in range(int(self.lot / in_row)):
            row += f'{"*" * in_row} \\n'
        row += f'{"*" * (self.lot % in_row)}'
        return row


cell1 = Cell(12)
cell2 = Cell(3)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(3))
print(cell2.make_order(12))