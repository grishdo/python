int_month = int(input('Введите месяц в виде числа: '))

list_month = ['Зима', 'Весна', 'Лето', 'Осень']

dict_month = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето',
              8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

if 1 <= int_month <= 2 or int_month == 12:
    print(list_month[0])
elif 3 <= int_month <= 5:
    print(list_month[1])
elif 6 <= int_month <= 8:
    print(list_month[2])
elif 9 <= int_month <= 11:
    print(list_month[3])

value_dict = dict_month.get(int_month)

print(value_dict)
