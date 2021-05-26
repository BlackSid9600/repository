class Stationery:


    def __init__(self, title):
        self.title = title


class Pen(Stationery):


    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Выбрана {self.title}, отрисовка ручкой.')


class Pencil(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Выбранан {self.title}, отрисовка карандашом.')


class Hendline(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'Выбран {self.title}, отрисовка маркером.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
hendline = Hendline('маркер')

pen.draw()
pencil.draw()
hendline.draw()