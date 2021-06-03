class Data:


    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} {self.b + other.b}'

    def __mul__(self, other):
        return f'Пороизведение равно: {self.a * other.a} {self.b * other.b}'

a = Data(1, 2)
b = Data(2,-3)
print(a + b)
print(a * b)