def my_func(a, b, c):
    list_arg = [a, b, c]
    list_arg.sort(reverse=True)
    print(list_arg[0] + list_arg[1])


arguments = []
for i in range(3):
    arguments.append(int(input('Введите значение: ')))

my_func(arguments[0], arguments[1], arguments[2])
