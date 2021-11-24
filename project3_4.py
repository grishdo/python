def my_func(x, y):
    print(x ** y)
    for i in range(1):
        x = x * x
    print(1 / x)


x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число y: '))

my_func(x, y)
