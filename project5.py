revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

profit = revenue - costs
if profit > 0:
    print(f'Прибыль: {profit}')
    rent = profit / revenue
    print(f'Рентабельность: {rent}')
    num_employ = int(input('Введите количество сотрудников: '))
    profit_num_employ = profit / num_employ
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {profit_num_employ}')
elif profit == 0:
    print(f'Точка безубыточности: {profit}')
else:
    print(f'Убыток: {profit}')
