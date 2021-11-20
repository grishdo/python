a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
day = 1

while True:
    print(f'{day}-й день: {"%.2f" % a}')
    if a < b:
        a = a + (a * 0.1)
        day += 1
    else:
        break

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
