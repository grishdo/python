with open("text.txt", "w", encoding='utf-8') as f:
    for i in range(11):
        f.write(f'{i} ')

with open("text.txt", "r", encoding='utf-8') as f:
    string = f.readline().split()
    print(sum(map(int, string)))

