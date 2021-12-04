with open("text.txt", "w", encoding='utf-8') as f:
    num_staff = int(input('Введите количество сотрудников: '))
    for i in range(num_staff):
        last_name_salary = input('Введите фамилию сотрудника и оклад: ')
        f.write(f'{last_name_salary}\n')

with open("text.txt", "r", encoding='utf-8') as f:
    num_str = f.readlines()
    sum_salary = 0
    for string in num_str:
        list_string = string.split()
        salary = int(list_string[1])
        if salary < 20000:
            print(f'У сотрудника {list_string[0]} оклад менее 20000')
        sum_salary += salary
    len_num_str = len(num_str)
    if len_num_str > 0:
        print(f'Средняя величина дохода сотрудников : {sum_salary / len_num_str}')




