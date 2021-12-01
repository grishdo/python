from itertools import count, cycle


def iterator_count():
    quit = int(input('Введите число для выхода: '))
    for i in count(int(input('Введите число: '))):
        print(i)
        if i == quit:
            break


def iterator_cycle():
    my_list = [1, 'F', 'B']
    j = int(input('Введите количество итераций: '))
    i = 0
    for el in cycle(my_list):
        if j == i:
            break
        print(el)
        i += 1


iterator_cycle()
iterator_count()
