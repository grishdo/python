with open("text.txt", "w") as f:
    string = ' '
    while string != '\n':
        string = f'{input("Введите строку: ")}\n'
        f.write(string)
