class OnlyNum(Exception):
    def __init__(self, txt):
        self.txt = txt


def create_num_list():
    num_list = []
    while True:
        value = input('Введите значение: ')
        if value == 'stop':
            return num_list
            break
        if value.isdigit():
            num_list.append(int(value))
        else:
            try:
                raise OnlyNum('Вы ввели не число')
            except OnlyNum as err:
                print(err)


print(create_num_list())
