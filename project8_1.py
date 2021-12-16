from datetime import date


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def type_data(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return day, month, year
        except ValueError:
            return 'Неверный формат даты'

    @staticmethod
    def valid(data):
        try:
            day, month, year = map(int, data.split('-'))
            date(year, month, day)
            return 'Корректно введенная дата'
        except ValueError:
            return 'Неверный формат даты'


print(Data.type_data('16-12-2021'))
print(Data.valid('16-12-2021'))
