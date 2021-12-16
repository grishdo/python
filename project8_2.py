class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(num, denom):
    try:
        if denom == 0:
            raise DivisionByZero('Деление на ноль')
    except DivisionByZero as err:
        print(err)
    else:
        print(num / denom)


num = int(input('Введите числитель: '))
denom = int(input('Введите знаменатель: '))
division(num, denom)
