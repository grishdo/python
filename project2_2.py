my_list = []

num_values = int(input('Введите количество значений в списке: '))

i = 0
while i < num_values:
    value = input('Введите значение: ')
    my_list.append(value)
    i += 1

print(my_list)

my_list_len = len(my_list)
flag = False
el = ''
i = 0

while i < my_list_len:
    if flag:
        el_1 = my_list[i]
        my_list[i] = el
        my_list[i - 1] = el_1
        flag = False
    else:
        el = my_list[i]
        flag = True
    i += 1

print(my_list)


