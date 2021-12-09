class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость! Ваша скорость: {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена скорость! Ваша скорость: {self.speed}')
        else:
            print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town = TownCar(55, 'blue', 'Audi', False)
town.go(), town.show_speed(), town.turn('Налево'), town.turn('Направо'), town.stop()
town.show_speed()

police = PoliceCar(70, '', 'BMW')
print(police.name, police.speed, police.is_police)
