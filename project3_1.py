def division(a, b):
    if b == 0:
        return 'Ошибка: деление на 0'
    else:
        return a / b


a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))

print(division(a, b))
