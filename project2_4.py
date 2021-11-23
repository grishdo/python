text = input('Введите несколько слов через пробел: ')

text = text.split()
index = 0
for i in text:
    if len(i) > 10:
        print(f'{index + 1} {i[:10]}')
    else:
        print(f'{index + 1} {i}')
    index += 1
