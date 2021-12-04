with open("text.txt", "r", encoding='utf-8') as f:
    num_str = f.readlines()
    print(f'Количество строк: {len(num_str)}')
    i = 1
    for string in num_str:
        print(f'Количество слов в строке {i}: {len(string.split())}')
        i += 1


