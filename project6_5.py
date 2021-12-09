class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {self.title}')


pen = Pen('ручкой')
pen.draw()

pencil = Pencil('карандашом')
pencil.draw()

handle = Handle('маркером')
handle.draw()
