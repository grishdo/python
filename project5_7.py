with open("text.txt", "r", encoding='utf-8') as f:
    all_profit = 0
    num_comp = 0
    dict_comp = {}
    dict_average = {}
    list_comp = []
    for line in f:
        company = line.split()[0]
        revenue = int(line.split()[2])
        costs = int(line.split()[3].replace('.', ''))
        profit = revenue - costs
        print(f'Прибыль компании {company}: {profit}')
        if profit > 0:
            all_profit += profit
            num_comp += 1
        dict_comp[company] = profit
    dict_average['average_profit'] = all_profit / num_comp
    list_comp.append(dict_comp)
    list_comp.append(dict_average)
    print(list_comp)


