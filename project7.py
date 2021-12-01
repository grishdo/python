def fact(num):
    factorial_num = 1
    for i in range(1, num + 1):
        factorial_num *= i
        yield f'{i}! = {factorial_num}'


for el in fact(int(input('Введите число: '))):
    print(el)
