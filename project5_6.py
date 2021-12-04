with open("text.txt", "r", encoding='utf-8') as f:
    sub_dict = {}
    for line in f:
        subject, hours = line.split(':')
        list_hours = [el for el in hours if el.isdigit() or el == '(']
        hours = sum(map(int, ''.join(list_hours).replace('(', ' ').split()))
        sub_dict[subject] = hours

    print(sub_dict)
