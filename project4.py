num = input('Введите число: ')

num_len = len(num)
i = 0

while i < num_len:
    if i == 0:
        num_check = int(num[i])
    else:
        if num_check < int(num[i]):
            num_check = int(num[i])
    i += 1

print(num_check)
