from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        for i, j in enumerate(cycle(TrafficLight.__color)):
            print(j)
            if j == 'Красный':
                sleep(7)
            elif j == 'Желтый':
                sleep(2)
            elif j == 'Зеленый':
                sleep(10)
            if i == 10:
                break


t = TrafficLight()

t.running()
