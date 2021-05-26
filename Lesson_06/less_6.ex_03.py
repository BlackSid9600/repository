class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name, self.surname}')

    def get_total_income(self):
        x = self._income['wage'] + self._income['bonus']
        print(f'Доход с учетом премим {x}')


den = Position('Den', 'Marshall', 'Дирктор', 500, 100)
sid = Position('Sid', 'Jackson', 'Заместитель дирктора', 400, 70)
ron = Position('Ron', 'Hubbard', 'Главный бухгалтер', 50, 55)

den.get_full_name(), den.get_total_income()
sid.get_full_name(), sid.get_total_income()
sid.get_full_name(), ron.get_total_income()
