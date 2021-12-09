class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}')


pos = Position('Иван', 'Иванов', 'Программист', 100000, 50000)
pos.get_full_name()
pos.get_total_income()
